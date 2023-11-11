// ImageUploader.js
import React, { useState } from "react";

const ImageUploader = () => {
  const [uploadStatus, setUploadStatus] = useState(""); // State to track upload status

  const handleUploadClick = async () => {
    try {
      // URL of your Flask API endpoint
      const apiUrl = "http://127.0.0.1:5000/api/extract_text_image";

      // File path to be sent in the POST request
      // const fileInput = document.getElementById("fileInput");
      // const file = fileInput.files[0];
      const filePath = "frontend/testing.png";

      // Create a FormData object and append the file
      const formData = new FormData();
      formData.append("file", filePath);

      // Make the POST request
      const response = await fetch(apiUrl, {
        method: "POST",
        body: formData,
      });

      // Check if the request was successful (status code 2xx)
      if (response.ok) {
        const data = await response.json();
        setUploadStatus(`${JSON.stringify(data)}`);
      } else {
        setUploadStatus(`Upload failed. Error: ${response.statusText}`);
      }
    } catch (error) {
      setUploadStatus(`Upload 2 failed. Error: ${error}`);
    }
  };

  return (
    <div>
      <button onClick={handleUploadClick}>Upload Image</button>
      <p>{uploadStatus}</p>
    </div>
  );
};

export default ImageUploader;