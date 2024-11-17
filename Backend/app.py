import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from urllib.parse import unquote  # To URL-decode the image name
from rekognition import process_image_from_s3  # Updated import for the new file name

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
outputFolder = 'outputimages/'

# Ensure output folder exists for saving processed images
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

@app.route('/')
def index():
    return "Car Detection API: Use /<image_name> to detect cars in an S3 image."

@app.route('/<image_name>', methods=['GET'])
def process_image(image_name):
    """
    Process the image specified by <image_name> in the S3 bucket
    and return the car count and URL to the processed image.
    """
    try:
        # URL-decode the image name to handle spaces and special characters
        decoded_image_name = unquote(image_name)
        
        # Debug: Print the decoded image name and the S3 key we are trying to access
        print(f"Decoded image name: {decoded_image_name}")
        print(f"S3 Key: {decoded_image_name}.jpg")  # This should match the exact path in S3

        # Process the image by calling the process_image_from_s3 function
        car_count, output_image_path = process_image_from_s3(decoded_image_name)

        # Save the processed image to the output folder
        output_image_name = os.path.basename(output_image_path)
        processed_image_path = os.path.join(outputFolder, output_image_name)

        # Move the image to the output folder (since it's saved in /tmp by default)
        os.rename(output_image_path, processed_image_path)

        # Return the processed image path and car count
        return jsonify({
            "car_count": car_count,
            "image_url": f"/uploads/{output_image_name}"
        })
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print for error
        return jsonify({"error": str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Serve the processed image from the output folder
    return send_from_directory(outputFolder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
