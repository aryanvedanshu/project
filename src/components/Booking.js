import React from 'react';
import './Button.css'; // Import the CSS file


const Button = ({ text, onClick, variant = 'black', className = '', type = 'button', disabled = false }) => {
  const buttonClass = variant === 'black' ? 'button button-black' : 'button button-orange';

  return (
    <button
      type={type}
      disabled={disabled}
      className={`${buttonClass} ${className}`}
      onClick={onClick}
    >
      {text}
    </button>
  );
};

export default Button;
