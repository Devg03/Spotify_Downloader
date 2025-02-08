import {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [val, setVal] = useState("");
  
  const click = () => {
    if (val.length > 0) {
      alert("Submitted!");
    } else {
      alert("Please enter a valid track ID.")
    }
  }

  const change = event => {
    const spotiURL = event.target.value;
    setVal(spotiURL);
  }

  return (
    <div className = "App">
      <h1>Please enter the Spotify track ID: </h1>
      <input onChange = {change} value = {val} />
      <button onClick = {click}>Submit!</button>
    </div>
  );
}

export default App;
