import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import Heading from './Navbar'

function App() {
  const [image, setImage] = useState();
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  const uploadImage = e => {
    setImage(e.target.files[0])
    fetch('/model', {
      method: "POST", 
      mode:"cors",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({image: {image}})
    })
  }

  return (
    <div className="App">
      <Heading />
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
      </header>
     <div className="upload_image">
        <input id="userImage" type="file" accept="image/*" onChange={uploadImage}/>
      </div>
    </div>
  );
}

export default App;
