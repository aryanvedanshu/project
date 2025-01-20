import React from 'react';
import { Link } from 'react-router-dom';

const CityCard = ({ title, description, image }) => {
  return (
    <Link to={`/services/${title}`} style={{ textDecoration: 'none' }}>
      <div className="card mx-2" style={{ width: '100%', border: 'none', cursor: 'pointer' }}>
        <img src={image} className="card-img-top" alt={title} style={{ height: '100px', objectFit: 'cover' }} />
        <div className="card-body text-center">
          <h5 className="card-title font-bold">{title}</h5>
          <p className="card-text">{description}</p>
        </div>
      </div>
    </Link>
  );
};

export default CityCard;
