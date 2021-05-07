import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import Heading from './Navbar'

function App() {
  const [image, setImage] = useState('');

  const uploadImage = e => {
    const reader = new FileReader();
    var file = e.target.files[0];
    reader.onloadend = function() {
      // console.log('RESULT', reader.result)
      setImage(reader.result)
      fetch('/model', {
        method: "POST", 
        mode:"cors",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(reader.result)
      })
    }

    reader.readAsDataURL(file)
  }

  return (
    <div className="App">
      <Heading />
      <header className="App-header">
      </header>
      <div className="upload_image">
        <input id="userImage" type="file" accept="image/*" onChange={uploadImage}/>
      </div>
      <img src={image}></img>
    </div>
  );
}

export default App;
