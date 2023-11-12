// ImageUploader.js
import React, { useState } from "react";

const ImageUploader = () => {
  const [uploadStatus, setUploadStatus] = useState(""); // State to track upload status
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUploadClick = async (e) => {
    console.log("handleUploadClick called");
    e.preventDefault();

    try {
      // URL of your Flask API endpoint
      const apiUrl = "http://127.0.0.1:5000/api/extract_text/4";
      // setUploadStatus(`Upload 3 failed. Error: `);
      // File path to be sent in the POST request
      const fileInput = document.getElementById("fileInput");
      const file = fileInput.files[0];
      
      // const filePath = "frontend/testing.png";
      
      if (!file) {
        setUploadStatus("No file chosen.");
        return;
      }

      // Create a FormData object and append the file
      const formData = new FormData();
      formData.append("file", file);
      
      // Make the POST request
      const response = await fetch(apiUrl, {
        method: "POST",
        body: formData,
      });
      
      // Check if the request was successful (status code 2xx)
      if (response.ok) {
        const data = await response.text();
        // setUploadStatus(`${JSON.stringify(data)}`);
        // const jsonString = JSON.stringify(data);
        // const formattedString = data.replace(/\n/g, '<br>');
        // return (
        //   <div>
        //     <p>{formattedString}</p>
        //   </div>
        // );
        // setUploadStatus(formattedString); 

        
        // const formattedString = data.replace(/\n/g, '<br>');
        document.getElementById('just-line-break').innerHTML = data +""
      //   setUploadStatus(data+"");
      // } else {
        setUploadStatus(`Upload failed. Error: ${response.statusText}`);
      }
    } catch (error) {
      setUploadStatus(`Upload 2 failed. Error: ${error}`);
    }
  };
  
  return (
    <div className="uploadPage">
      <input className="uploadButton" type="file" id="fileInput" onChange={handleFileChange}/>
      <button className="uploadButton" onClick={handleUploadClick}>Upload Image</button>
      {/* <p>{uploadStatus}</p> */}
      <div className="uploadPage" id="just-line-break"></div>
    </div>
  );
};

export default ImageUploader;
