import {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [val, setVal] = useState("");

  const change = event => {
    const spotiURL = event.target.value;
    setVal(spotiURL);
  }

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({input_data: val}),
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error: ', error);
    }
  };

  return (
    <div className = "App">
      <h1>Please enter the Spotify track ID: </h1>
      <input type = 'text' onChange = {change} value = {val} />
      <button type = 'submit' onClick = {handleSubmit}>Submit!</button>
    </div>
  );
}

export default App;
