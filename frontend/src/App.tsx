import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useAuth0, Auth0Provider } from "@auth0/auth0-react";
import Auth0ProviderWithHistory from './authy';
import ReactDOM from 'react-dom';

// ReactDOM.render(
//   <React.StrictMode>
//     <Auth0ProviderWithHistory>
//       <App />
//     </Auth0ProviderWithHistory>
//   </React.StrictMode>,
//   document.getElementById('root')
// );


const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return <button onClick={() => loginWithRedirect()}>Log In</button>;
};

function App() {
  // const { loginWithRedirect } = useAuth0();
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        

        {/* <button onClick={() => loginWithRedirect()}>Log In</button> */}
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

const Login = () => {
  const { loginWithRedirect } = useAuth0();

  return (
    <div className="App">
      <div className='Info'>
        <h2 className="App-header">
          Jotter
        </h2>
        <button className='logIn' onClick={() => loginWithRedirect()}>Log In</button>
      </div>
    </div>
  );
};

export default Login;
