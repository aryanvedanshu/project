import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';

const Profile = () => {
  return (
    <div className="profile">
      <h2>Your Profile</h2>
      <p>Manage your personal information and preferences.</p>
      <Link to="/edit-profile">
      <Button text="Edit Profile" />
      <br />
      <br />
      <Button text="Log Out" />
      </Link>
    </div>
  );
};

export default Profile;
