import './App.css';
import { useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter, Router, Route} from "react-router-dom";
import Header from './components/Header';
import HomePage from "./main";
function App() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/">
                    <Route index element={<HomePage />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
