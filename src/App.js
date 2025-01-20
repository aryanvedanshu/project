import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Block from './components/Block';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/block" element={<Block />} />
      {/* Add more routes here */}
    </Routes>
  );
};

export default App;
