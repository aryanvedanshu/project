import React from 'react';
import Home from '../components/Home';
import Login from '../components/Login';
import Register from '../components/Register';
import Profile from '../components/Profile';
import EditProfile from '../components/Profile';
import Services from '../components/Services';
import Booking from '../components/Booking';
import Location from '../components/Location';
import Community from '../components/Community';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


export const Routes = () => {
  return (
    <Router>
    <Switch>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/services/:cityName" component={Services} /> {/* Dynamic route for services */}
      <Route path="/edit-profile" element={<EditProfile />} />
      <Route path="/services" element={<Services />} />
      <Route path="/booking" element={<Booking />} />
      <Route path="/location" element={<Location />} />
      <Route path="/community" element={<Community />} />
    </Switch>
    </Router>
  );
};
