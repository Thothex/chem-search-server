import { FC } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import logo from '../assets/logo.svg';
import '../styles/components/Header.scss';

const Header: FC = () => {
    const navigate = useNavigate();
    const location = useLocation(); // Получаем текущий путь

    const handleNavigate = (path: string) => {
        navigate(path);
    };

    const getButtonClass = (path: string) => {
        return location.pathname === path ? "active" : "";
    };

    return (
        <div className="header">
            <img src={logo} alt='logo'/>
            <nav>
                <button className={getButtonClass("/")} onClick={() => handleNavigate("/")}>Home</button>
                <button className={getButtonClass("/about")} onClick={() => handleNavigate("/about")}>About</button>
                <button className={getButtonClass("/docs")} onClick={() => handleNavigate("/docs")}>Docs</button>
                <button className={getButtonClass("/login")} onClick={() => handleNavigate("/login")}>Sign in</button>
                <button className={getButtonClass("/register")} onClick={() => handleNavigate("/register")}>Sign up</button>
            </nav>
            <button id='save'></button>
        </div>
    );
}

export default Header;
