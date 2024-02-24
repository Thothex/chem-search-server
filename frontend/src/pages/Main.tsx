import  {FC} from "react";
import '../styles/pages/Main.scss'
import Header from "../components/Header.tsx";

const Main :FC = () =>{
    return(
        <div className="main">
        <div className="article">
            <Header />
            <div className="search">
                <button id='save'></button>
                <input type="text" placeholder="Search..."/>
                <button id='draw'></button>
            </div>
        </div>
        </div>
    )
}

export default Main;
