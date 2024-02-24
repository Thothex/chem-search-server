import { FC } from "react";
import logo from '../assets/logo.svg';
import AuthButton from '../components/AuthButton';
import '../styles/pages/AuthPage.scss';
import { useNavigate } from "react-router-dom";

const Login: FC = () => {
    const navigate = useNavigate();

    const handleNavigate = (path: string) => {
        navigate(path);
    }

    return (
        <div className='authPage'>
            <img src={logo} alt='logo' />
            <h1>Log into your account</h1>
            <p>Welcome back! Please fill all the fields.</p>
            <form>
                <label>
                    <span>Email</span>
                    <input type="email" placeholder="Enter your email" />
                </label>
                <label>
                    <span>Password</span>
                    <input type="password" placeholder="Enter your password" />
                </label>
                <div>
                    <div>
                        <input type="checkbox" id="remember" />
                        <label htmlFor="remember">Remember me</label>
                    </div>
                    <span>Forgot password</span>
                </div>
                <AuthButton buttonText="Sign in" />
            </form>
            <h5>Don't have an account? <button onClick={() => handleNavigate("/register")}>Sign up</button></h5>
        </div>
    );
}

export default Login;
