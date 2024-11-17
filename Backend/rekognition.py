import boto3
from PIL import Image, ImageDraw
import io
import os

# AWS Setup
rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

# S3 Bucket details
bucketName = "actioncameradata"
image_base_path = "parking_rois_gopro/images/"  # Path where images are stored in S3

# Ensure output folder exists for saving processed images
outputFolder = 'outputimages/'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

def process_image_from_s3(image_name):
    """
    Process an image stored in S3, detect cars, and return the car count and processed image.
    """
    try:
        # Construct the full S3 key for the image, including the folder path
        image_key = f"{image_base_path}{image_name}.jpg"  # e.g., parking_rois_gopro/images/<image_name>.jpg
        
        # Debugging: Print the full S3 key
        print(f"Attempting to fetch image from S3 with key: {image_key}")

        # Fetch image from S3
        s3_response = s3.get_object(Bucket=bucketName, Key=image_key)
        image_data = s3_response['Body'].read()  # Read image data

        # Open the image using PIL from the bytes
        image = Image.open(io.BytesIO(image_data))
        draw = ImageDraw.Draw(image)

        # Call Amazon Rekognition to detect objects in the image (detecting labels and bounding boxes)
        detectLabelsResponse = rekognition.detect_labels(
            Image={'Bytes': image_data},
            MaxLabels=100,
            MinConfidence=80
        )

        car_count = 0

        # Iterate through the labels and check for "Car" with bounding boxes
        for label in detectLabelsResponse["Labels"]:
            if label["Name"] == "Car":
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

        # Save the output image with bounding boxes to the output folder
        output_image_path = os.path.join(outputFolder, f"{image_name}_output_with_boxes.png")
        image.save(output_image_path)

        # Return the car count and the processed image path
        return car_count, output_image_path

    except Exception as e:
        print(f"Error processing image from S3: {str(e)}")
        raise Exception(f"Error processing image from S3: {str(e)}")
