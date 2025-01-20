import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">Room Adda</div>
      <div className="links">
        <Link to="/">
          <Button text="Home" className="orange-black" />
        </Link>
        <Link to="/services">
          <Button text="Services" className="orange-black" />
        </Link>
        <Link to="/profile">
          <Button text="Profile" className="orange-black" />
        </Link>
        <Link to="/login">
          <Button text="Login" className="orange-black" />
        </Link>
        <Link to="/register">
          <Button text="Register" className="orange-black" />
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
