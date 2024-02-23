import {FC} from "react";
import logo from '../assets/logo.svg';
import AuthButton from '../components/AuthButton';
import '../styles/pages/AuthPage.scss';
const Login : FC = () => {
    return(
        <div className='authPage'>
            <img src={logo} alt='logo'/>
            <h1>Log in to your account</h1>
            <p>Welcome back! Please fill all the fields.</p>
            <form>
            <label> Email
            <input type="email" placeholder="Enter your email"/>
            </label>
            <label> Password
                <input type="password" placeholder="Enter your password"/>
            </label>
            <span>remember</span>
            <AuthButton buttonText="Sign in" />
        </form>
        </div>
    )

}

export default Login;
