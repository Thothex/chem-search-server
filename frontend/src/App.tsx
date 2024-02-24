import Login from "./pages/Login.tsx";
import Register from "./pages/Register.tsx";
import Main from "./pages/Main.tsx";
import {Route, Routes} from "react-router-dom";

function App() {
    return (
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
            </Routes>
    );
}

export default App
