import boto3
from IPython.display import HTML, display, Image as IImage
from PIL import Image, ImageDraw, ImageFont
import time
import os

# Current AWS Region. Use this to choose corresponding S3 bucket with sample content
mySession = boto3.session.Session()
awsRegion = mySession.region_name

# Init clients
rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

# S3 bucket that contains sample images and videos
bucketName = "actioncameradata"

# Create temporary directory
tempFolder = 'm1tmp/'
if not os.path.exists(tempFolder):
    os.makedirs(tempFolder)

imageName = "parking_rois_gopro/images/GOPR0103.JPG"

# Display the image
display(IImage(url=s3.generate_presigned_url('get_object', Params={'Bucket': bucketName, 'Key': imageName})))

# Download the image to our temporary directory
localPath = os.path.join(tempFolder, "cars.png")
s3.download_file(bucketName, imageName, localPath)

# Open the image using PIL
image = Image.open(localPath)
draw = ImageDraw.Draw(image)

# Call Amazon Rekognition to detect objects in the image (detecting labels and bounding boxes)
detectLabelsResponse = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': bucketName,
            'Name': imageName,
        }
    },
    MaxLabels=100,  # Optional: You can set MaxLabels to a higher value if you expect many objects
    MinConfidence=50  # Optional: Adjust this value based on the confidence level you want
)

# Count the number of "Car" labels using bounding boxes (each bounding box corresponds to a car detected)
car_count = 0

# Iterate through the labels and check for "Car" with bounding boxes
for label in detectLabelsResponse["Labels"]:
    if label["Name"] == "Car":
        # Each "Instances" entry represents a detected car with a bounding box
        for instance in label.get("Instances", []):
            # Extract the bounding box coordinates
            box = instance["BoundingBox"]
            left = box["Left"] * image.width
            top = box["Top"] * image.height
            width = box["Width"] * image.width
            height = box["Height"] * image.height

            # Draw the bounding box on the image
            draw.rectangle([left, top, left + width, top + height], outline="red", width=3)

            # Increment the car count
            car_count += 1

# Print the number of cars detected
print(f"Number of cars detected: {car_count}")

# Save the image with bounding boxes to the temporary directory
output_image_path = os.path.join(tempFolder, "cars_with_boxes.png")
image.save(output_image_path)

# Display the saved image
display(IImage(output_image_path))
