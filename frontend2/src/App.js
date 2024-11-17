import { BrowserRouter, Routes, Route} from "react-router-dom";
import "./App.css"
import HomePage from "./Main";
import Page from "./Page";

function App() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/">
                    <Route index element={<HomePage />} />
                    <Route path="/page/:title" element={<Page />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
