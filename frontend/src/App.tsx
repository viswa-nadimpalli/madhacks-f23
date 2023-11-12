import React from 'react'
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom'
import FirstPage from './Firstpage'
import SecondPage from './ImageUploader'
import Quiz from './Quiz'
import Authy from './authy'
import './App.css';
import { useAuth0, Auth0Provider } from "@auth0/auth0-react";
import './fonts/Ubuntu/Ubuntu-Bold.ttf';
import './lAni.css';

const App = () => {
  const { loginWithRedirect, isAuthenticated, user, isLoading } = useAuth0();

  if (isLoading) {
    const loading = document.querySelector('.loading-container');
    loading && loading.classList.add('loadanimate');

    return(
      <div className='bod'>
      <div className="loading-container loadanimate">
        <div className="loading-spinner">Loading<span className="ellipsis">...</span></div>
      </div>
      </div>
    );
  }
  const updateDB = async () => {
    try {
      const username = user?.name;
      const id = user?.sub;
      // URL of your Flask API endpoint
      const apiUrl = `http://127.0.0.1:5000/api/newUser/${username}/${id}`;
      // setUploadStatus(`Upload 3 failed. Error: `);
      // File path to be sent in the POST request
  
  
      // Make the POST request
      let sends = 0;
      if (sends === 0){ 
      const response = await fetch(apiUrl, {
        method: "POST"
      })
      console.log(response);
      sends += 1;
    }
    }
    catch {
      console.log('damn');
    }
    };
  
    if (isAuthenticated && user) {
      const val = updateDB();
      console.log(val)
    }

  if (isAuthenticated && user) {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<SecondPage/>} />
          <Route path="/info" element={<SecondPage/>} />
          <Route path="/home" element={<FirstPage/>} />
          <Route path="/quiz" element={<Quiz/>} />
        </Routes >
      </Router>
    );
  }



  return (
    <Router>
      <Routes>
        <Route path="/" element={<FirstPage/>} />
        <Route path="/info" element={<SecondPage/>} />
        <Route path="/home" element={<FirstPage/>} />
        <Route path="/quiz" element={<Quiz/>} />
      </Routes >
    </Router>
  );
};

export default App;