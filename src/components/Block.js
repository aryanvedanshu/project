import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const Block = () => {
  const navigate = useNavigate(); // Use navigate for navigation

  const cities = [
    { name: 'Delhi', image: 'path/to/delhi-image.jpg', description: 'Capital city of India' },
    { name: 'Mumbai', image: 'path/to/mumbai-image.jpg', description: 'Financial capital of India' },
    { name: 'Bengaluru', image: 'path/to/bengaluru-image.jpg', description: 'Silicon Valley of India' },
    // Add more cities as needed
  ];

  return (
    <div className="container mt-5">
      <h2 className="text-center">Select Your City</h2>
      <div className="row">
        {cities.map((city) => (
          <div className="col-md-3 mb-3" key={city.name}>
            <div className="card text-center">
              <img src={city.image} alt={city.name} className="card-img-top" />
              <div className="card-body">
                <h5 className="card-title">{city.name}</h5>
                <p className="card-text">{city.description}</p>
                <button 
                  className="btn btn-primary" 
                  onClick={() => navigate(`/services/${city.name}`)} // Navigate to services page with city name
                >
                  View Services
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Block;
