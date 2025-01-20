import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">Room Adda</div>
      <div className="links">
        <Link to="/">
          <Button text="Home" />
        </Link>
        <Link to="/services">
          <Button text="Services" />
        </Link>
        <Link to="/profile">
          <Button text="Profile" />
        </Link>
        <Link to="/login">
          <Button text="Login" />
        </Link>
        <Link to="/register">
          <Button text="Register" />
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
