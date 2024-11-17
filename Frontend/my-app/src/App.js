import { BrowserRouter, Routes, Route} from "react-router-dom";
import "./App.css"
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
