import React from 'react';
import Carousel from './components/Carousel';
import Header from './components/Header';
import Footer from './components/Footer';
import Block from './components/Block';

const Home = () => {
  return (
    <div className="container mx-auto p-4">
      <Header />
      <Carousel />

      <h1 className="text-4xl font-bold mb-6 text-center">Welcome to Room Adda</h1>

      <div className="mb-6 text-center">
        <label htmlFor="location" className="text-lg">Enter your college name or location for relevant searches in the area:</label>
        <input 
          type="text" 
          id="location" 
          placeholder="Search..." 
          className="border border-gray-300 p-2 ml-2"
        />
      </div>

      <Block />

      <Footer />
    </div>
  );
};

export default Home;
