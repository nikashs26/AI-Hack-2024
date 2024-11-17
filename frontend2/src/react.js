import React, { useState } from 'react';
import axios from 'axios';

const ImageProcessor = () => {
const [imageName, setImageName] = useState('');
const [carCount, setCarCount] = useState(null);
const [imageUrl, setImageUrl] = useState('');

// Handle form submit to request image processing
const handleSubmit = async (e) => {
e.preventDefault();

try {
// Make GET request to Flask backend to process the image
const response = await axios.get(`http://127.0.0.1:5000/${imageName}`);

// Set car count and image URL from the JSON response
setCarCount(response.data.car_count);
setImageUrl(`http://127.0.0.1:5000${response.data.image_url}`);
} catch (error) {
console.error('Error processing image:', error);
alert('Error processing image');
}
};

return (
<div>
<h1>Process Image with Rekognition</h1>
<form onSubmit={handleSubmit}>
<input
type="text"
value={imageName}
onChange={(e) => setImageName(e.target.value)}
placeholder="Enter image name"/>
<button type="submit">Process Image</button>
</form>

{carCount !== null && (
<div>
<h2>Car Count: {carCount}</h2>
<img src={imageUrl} alt="Processed Image" />
</div>
)}
</div>
);
};

export default ImageProcessor;