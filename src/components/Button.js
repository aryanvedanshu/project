import React from 'react';
import './Button.css'; // Import the CSS file for button styles

const Button = ({ text, onClick, className = 'orange-black' }) => {
  return (
    <button className={`custom-btn ${className}`} onClick={onClick}>
      {text}
    </button>
  );
};

export default Button;
