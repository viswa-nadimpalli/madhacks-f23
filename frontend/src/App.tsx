import React from 'react'
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom'
import FirstPage from './Firstpage'
import SecondPage from './ImageUploader'
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


  if (isAuthenticated && user) {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<SecondPage/>} />
          <Route path="/home" element={<FirstPage/>} />
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
      </Routes >
    </Router>
  );
};

export default App;