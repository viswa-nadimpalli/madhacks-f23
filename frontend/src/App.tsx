import React from 'react'
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom'
import FirstPage from './firstpage'
import Test from './App.test'


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FirstPage />} />
        {/* <Route path="/info" element={<SecondPage />} /> */}
      </Routes >
    </Router>
  );
};

export default App;