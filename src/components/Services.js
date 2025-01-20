import React from 'react';
import { useParams } from 'react-router-dom';

const Services = () => {
  const { cityName } = useParams(); // Get the city name from the URL

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-4xl font-bold mb-6 text-center">Services in {cityName}</h1>
      {/* Implement your filtering logic here */}
    </div>
  );
};

export default Services;
