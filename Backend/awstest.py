# # Initialise Notebook
# import boto3
# from IPython.display import HTML, display, Image as IImage
# from PIL import Image, ImageDraw, ImageFont
# import time
# import os

# # Curent AWS Region. Use this to choose corresponding S3 bucket with sample content

# mySession = boto3.session.Session()
# awsRegion = mySession.region_name

# # Init clients
# rekognition = boto3.client('rekognition')
# s3 = boto3.client('s3')

# # S3 bucket that contains sample images and videos

# # We are providing sample images and videos in this bucket so
# # you do not have to manually download/upload test images and videos.

# bucketName = "aws-rek-immersionday-" + awsRegion

# # Create temporary directory
# # This directory is not needed to call Rekognition APIs.
# # We will only use this directory to download images from S3 bucket and draw bounding boxes

# tempFolder = 'm1tmp/'

# imageName = "media/object-detection/cars.png"

# display(IImage(url=s3.generate_presigned_url('get_object', Params={'Bucket': bucketName, 'Key': imageName})))

# # Download the image to our temporary directory
# localPath = "m1tmp/cars.png"
# s3.download_file(bucketName, imageName, localPath)

# # Call Amazon Rekognition to detect objects in the image
# # https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html

# detectLabelsResponse = rekognition.detect_labels(
#     Image={
#         'S3Object': {
#             'Bucket': bucketName,
#             'Name': imageName,
#         }
#     }
# )

# # Show JSON response returned by Rekognition Labels API (Object Detection)
# # In the JSON response below, you will see Label, detected instances, confidence score and additional information.

# display(detectLabelsResponse)

# flaggedObjects = ["Car"]

# for label in detectLabelsResponse["Labels"]:
#     if(label["Name"] in flaggedObjects):
#         print("Detected unsafe object:")
#         print("- {} (Confidence: {})".format(label["Name"], label["Confidence"]))
#         print("  - Parents: {}".format(label["Parents"]))

# imagePropertiesResponse = rekognition.detect_labels(
#     Image={
#         'S3Object': {
#             'Bucket': bucketName,
#             'Name': imageName,
#         }
#     },
#     Features=["IMAGE_PROPERTIES"], # 'GENERAL_LABELS',
#     Settings={
#         "ImageProperties": {
#             "MaxDominantColors": 10
#         }
#     }
# )

# # Show JSON response returned by Rekognition Labels API (Object Detection)
# # In the JSON response below, you will see Image Properties, sharpness, brightness, contrast and additional information.

# display(imagePropertiesResponse)

# # Get image size and DPI (Dots per Inch) using Pillow
# im = Image.open('m1tmp/cars.png')
# print(f'Image size: {im.size[0]} X {im.size[1]}')
# print(f'DPI: {im.info["dpi"]}')

# # Image quality from Rekognition
# print('Quality: ')
# print(f'     Brightness: {round(imagePropertiesResponse["ImageProperties"]["Quality"]["Brightness"],2)}%')
# print(f'     Sharpness: {round(imagePropertiesResponse["ImageProperties"]["Quality"]["Sharpness"],2)}%')
# print(f'     Contrast: {round(imagePropertiesResponse["ImageProperties"]["Quality"]["Contrast"],2)}%')

# print('Dominant Colors: ')
# for c in imagePropertiesResponse["ImageProperties"]["DominantColors"]:
#     html = f'''<div style="background-color:{c['HexCode']};width:250px;margin-left:60px;padding-left:5px;">RGB({c['Red']},{c['Green']},{c['Blue']}])  {round(c["PixelPercent"],2)}%</div>'''
#     display(HTML(html))

# Initialise Notebook
# Initialise Notebook
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
bucketName = "aws-rek-immersionday-" + awsRegion

# Create temporary directory
tempFolder = 'm1tmp/'

imageName = "media/object-detection/cars.png"

# Display the image
display(IImage(url=s3.generate_presigned_url('get_object', Params={'Bucket': bucketName, 'Key': imageName})))

# Download the image to our temporary directory
localPath = "m1tmp/cars.png"
s3.download_file(bucketName, imageName, localPath)

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
        car_count += len(label.get("Instances", []))

# Print the number of cars detected
print(car_count)
