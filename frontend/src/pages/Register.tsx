import {FC} from "react";
import logo from '../assets/logo.svg';
import AuthButton from '../components/AuthButton';
import '../styles/pages/AuthPage.scss';
const Register : FC = () => {
    return(
        <div className='authPage'>
            <img src={logo} alt='logo'/>
            <h1 style={{paddingBlock:'.5em .5em'}}>Create an account</h1>
            <form>
                <label> <span>Email</span>
                    <input type="email" placeholder="Enter your email"/>
                </label>
                <label> <span>Password</span>
                    <input type="password" placeholder="Enter your password"/>
                </label>
                <label> <span>Confirm password</span>
                    <input type="password" placeholder="Enter your password one more time"/>
                </label>
                <AuthButton buttonText="Sign in" />
            </form>
            <h5>Already have an account? <span>Log in</span></h5>
        </div>
    )

}

export default Register;
