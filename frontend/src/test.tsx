import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import FirstPage from "./Firstpage";
import SecondPage from "./ImageUploader";
import Test from "./test";
import Authy from "./authy";
import "./App.css";
import { useAuth0, Auth0Provider } from "@auth0/auth0-react";
import "./fonts/Ubuntu/Ubuntu-Bold.ttf";
import "./lAni.css";
import { useLocation } from 'react-router-dom'

const App = () => {
  const { loginWithRedirect, isAuthenticated, user, isLoading } = useAuth0();

  const updateDB = async () => {
    try {
        console.log("hi");
    } catch {
      console.log("damn");
    }
  };

  if (isAuthenticated && user) {
    const val = updateDB();
    console.log(val);
  }


  return (
    <Router>
      <Routes>
        <Route path="/" element={<FirstPage />} />
        <Route path="/info" element={<SecondPage />} />
        <Route path="/home" element={<FirstPage />} />
        <Route path="/test" element={<Test/>} />
        <Route path="/test" element={<Test />} />
      </Routes>
    </Router>
  );
};

const Tests: React.FC = () => {
  const location = useLocation();
  const data = new URLSearchParams(location.search).get("data") || "No data";

  return (
    <div>
      <p>{data}</p>
    </div>
  );
};

export default App;