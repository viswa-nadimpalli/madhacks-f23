// GeneratePDFPage.js

import React from 'react';

const GeneratePDFPage = () => {
  const redirectToPDF = () => {
    window.location.href = 'http://127.0.0.1:5000/generate_pdf';
  };

  return (
    <div>
      <button id='dnldButton' className="downloadButton gone" onClick={redirectToPDF}>Download PDF</button>
    </div>
  );
};

export default GeneratePDFPage;
