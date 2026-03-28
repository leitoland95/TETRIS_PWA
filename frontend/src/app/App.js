import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Tetris</h1>
      <canvas id="tetris-canvas" width={300} height={500}></canvas>
      <script src="https://unpkg.com/react-tetris"></script>
    </div>
  );
}

export default App;