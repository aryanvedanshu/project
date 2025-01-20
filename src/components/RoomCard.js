import React from 'react';
import Button from './Button';

const RoomCard = ({ title, description, price }) => {
  return (
    <div className="border p-4 rounded-lg shadow-lg">
      <h3 className="text-xl font-semibold">{title}</h3>
      <p className="text-gray-700">{description}</p>
      <p className="font-bold text-[#d48166]">Price: {price}</p>
      <Button text="Book Now" variant="orange" className="mt-2" />
    </div>
  );
};

export default RoomCard;
