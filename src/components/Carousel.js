import React, { useState, useEffect } from 'react';
import './Carousel.css';

const Carousel = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const slides = [
    { image: '/slide.png', heading: 'Welcome to Room Adda', paragraph: 'Find the best rooms for you!' },
    { image: '/slide.png', heading: 'PG and Single Rooms', paragraph: 'Affordable and accessible living spaces.' },
    { image: '/slide.png', heading: 'Studio Apartments', paragraph: 'Modern and spacious studio flats available.' },
    { image: '/slide.png', heading: 'Community of Students', paragraph: 'Join our community and find roommates.' },
    { image: '/slide.png', heading: 'Book Easily', paragraph: 'Quick and hassle-free room bookings.' },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev === slides.length - 1 ? 0 : prev + 1));
    }, 5000); // Change slide every 5 seconds
    return () => clearInterval(interval);
  }, [slides.length]);

  return (
    <div className="carousel h-screen relative">
      {slides.map((slide, index) => (
        <div
          key={index}
          className={`carousel-slide ${index === currentSlide ? 'active' : ''}`}
          style={{ backgroundImage: `url(${slide.image})` }}
        >
          <div className="carousel-text bg-black text-orange-500 p-4 absolute bottom-0 w-full text-center">
            <h2 className="text-2xl font-bold">{slide.heading}</h2>
            <p>{slide.paragraph}</p>
          </div>
        </div>
      ))}
      <div className="carousel-indicators">
        {slides.map((_, index) => (
          <span
            key={index}
            className={`indicator ${index === currentSlide ? 'active' : ''}`}
            onClick={() => setCurrentSlide(index)}
          ></span>
        ))}
      </div>
    </div>
  );
};

export default Carousel;
