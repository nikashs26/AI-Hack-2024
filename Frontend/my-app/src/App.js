import './App.css';
import { useEffect } from 'react';
import axios from 'axios';

import Header from './components/Header';

function App() {
  useEffect(() => {
    axios.get('/').then(response => {
        console.log(response.data);
    });
}, []);

return (
    <div>
        <h1>Frontend and Backend Connected!</h1>
    </div>
);
}

export default App;
