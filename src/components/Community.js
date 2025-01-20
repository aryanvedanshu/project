import React, { useState } from 'react';

const Community = () => {
  const [adDetails, setAdDetails] = useState({ roomType: '', price: '', contact: '' });

  const handlePostAd = (e) => {
    e.preventDefault();
    // Implement logic to post ad
  };

  return (
    <div className="community">
      <h2>Community Listings</h2>
      <form onSubmit={handlePostAd}>
        <input
          type="text"
          placeholder="Room Type"
          value={adDetails.roomType}
          onChange={(e) => setAdDetails({ ...adDetails, roomType: e.target.value })}
        />
        <input
          type="text"
          placeholder="Price"
          value={adDetails.price}
          onChange={(e) => setAdDetails({ ...adDetails, price: e.target.value })}
        />
        <input
          type="text"
          placeholder="Contact Info"
          value={adDetails.contact}
          onChange={(e) => setAdDetails({ ...adDetails, contact: e.target.value })}
        />
        <button type="submit">Post Ad</button>
      </form>
      {/* Listings of posted ads can be displayed here */}
    </div>
  );
};

export default Community;
