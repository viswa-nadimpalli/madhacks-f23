// ImageUploader.js
import React, { useState } from "react";
import GeneratePDFPage from './GeneratePDFPage';
var type1 = "0";
const ImageUploader = () => {
  const [uploadStatus, setUploadStatus] = useState(""); // State to track upload status
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const click1 = async (e) => {
    type1 = "1";
    document.getElementById("dropdown").innerHTML = "True or False";
  }

  const click2 = async (e) => {
    type1 = "2";
    document.getElementById("dropdown").innerHTML = "Multiple Choice";
  }

  const click3 = async (e) => {
    type1 = "3";
    document.getElementById("dropdown").innerHTML = "Short Answer";
  }

  const click4 = async (e) => {
    type1 = "4";
    document.getElementById("dropdown").innerHTML = "Cheat Sheet";
  }

  const handleUploadClick = async (e) => {
    console.log("handleUploadClick called");
    e.preventDefault();

    try {
      // URL of your Flask API endpoint
      
      const apiUrl = "http://127.0.0.1:5000/api/extract_text/"+type1;
      // const apiUrl = "http://127.0.0.1:5000/generate_pdf";
      // setUploadStatus(`Upload 3 failed. Error: `);
      // File path to be sent in the POST request
      const fileInput = document.getElementById("fileInput");
      const file = fileInput.files[0];
      
      // const filePath = "frontend/testing.png";
      if(type1=="0"){
        document.getElementById('just-line-break').innerHTML = "No option chosen.";
        return;
      }
      
      if (!file) {
        document.getElementById('just-line-break').innerHTML = "No file chosen.";
        return;
      }
      document.getElementById('just-line-break').innerHTML = "Loading...";
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
        if (type1=="4"){
          document.getElementById('just-line-break').innerHTML = "PDF Success!"
          // document.getElementById("downloadButton").style.visibility="‌​visible";
        } else {
          document.getElementById('just-line-break').innerHTML = data +""
        }
        
      //   setUploadStatus(data+"");
      } else {
        setUploadStatus(`Upload failed. Error: ${response.statusText}`);
      }
    } catch (error) {
      setUploadStatus(`Upload 2 failed. Error: ${error}`);
    }
  };


  
    return (
      <div className="uploadPage">

        <input className="uploadButton" type="file" id="fileInput" onChange={handleFileChange}/>
        <div class="dropdown">
          <button id="dropdown">Options</button>
          <div class="dropdown-content">
            <a href="#" onClick={click1}>True or False</a>
            <a href="#" onClick={click2}>Multiple Choice</a>
            <a href="#" onClick={click3}>Short Answer</a>
            <a href="#" onClick={click4}>Cheat Sheet</a>
          </div>
        </div>
        <button className="uploadButton" onClick={handleUploadClick}>Upload File</button>
        <GeneratePDFPage />
        <div className="uploadPage" id="just-line-break"></div>
      </div>
    );
  
};

export default ImageUploader;
