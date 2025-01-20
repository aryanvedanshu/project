import React, { useState } from 'react';

const EditProfile = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleUpdate = (e) => {
    e.preventDefault();
    // Implement update logic here
  };

  return (
    <div className="edit-profile">
      <h2>Edit Profile</h2>
      <form onSubmit={handleUpdate}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
};

export default EditProfile;
