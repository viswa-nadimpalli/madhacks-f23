import React, { useEffect } from 'react';
import logo from './imgs/graphic.png';
import './App.css';
import { useAuth0, Auth0Provider } from "@auth0/auth0-react";
import './fonts/Ubuntu/Ubuntu-Bold.ttf'
import { Link } from 'react-router-dom'
import './firstpage.css'
// ReactDOM.render(
//   <React.StrictMode>
//     <Auth0ProviderWithHistory>
//       <App />
//     </Auth0ProviderWithHistory>
//   </React.StrictMode>,
//   document.getElementById('root')
// );


// const LoginButton = () => {
//   const { loginWithRedirect } = useAuth0();

//   return <button onClick={() => loginWithRedirect()}>Log In</button>;
// };

const Login = () => {


  useEffect(() => {
    // Add the "animated" and "rise-up" classes on mount
    const info = document.querySelector('.Info');
    const text = document.querySelector('.App-header');
    const lgbutton = document.querySelector('.login');
    const st = document.querySelector('.subtext');
    const logoimg = document.querySelector('.logo');
    logoimg && logoimg.classList.add('rise-up');
    info && info.classList.add('animated');
    text && text.classList.add('rise-up');
    lgbutton && lgbutton.classList.add('button-animate');
    st && st.classList.add('stanimate');
  }, []); // Run the effect only once on mount


  // let userInfo = <h2 className='userinfo'>Buffer </h2>;
  // if (user && isAuthenticated) {
  //   userInfo = <h2 className='userinfo'>Welcome, {user.name}</h2>;
  //   const useranimate = document.querySelector('.userinfo');
  //   useranimate && useranimate.classList.add('usanimate');
  // }

const { loginWithPopup } = useAuth0();

  const handleLog = async () => {
    try {

      await loginWithPopup();


      window.location.href = '/info';

    }
    catch (error) {
      console.error('Login failed:', error);
    }
  }

  return (
    <div className="App">
      <div className='Info'>
        <div className='text'>
            <h2 className="App-header">Jotter</h2>
            <p className='subtext'>Your information assistant</p>
            <button className='login' onClick={handleLog}><b>Log In</b></button>
          {/* <Link to="/info">Click Here!</Link> */}
        </div>
        <img className='logo' src={logo} alt='icon'/>
        {/* <h1>Imagine an image is here lmao</h1> */}
      </div>
    </div>
  );
};

export default Login;