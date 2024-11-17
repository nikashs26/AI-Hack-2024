import { BrowserRouter, Routes, Route} from "react-router-dom";
import "./App.css"
import HomePage from "./Main";

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
