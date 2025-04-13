import React from 'react';
import './SendButton.css';

const SendButton = ({ text = "Enviar Avaliação", onClick }) => {
  return (
      <button className="blue-button" onClick={onClick}>
        {text}
      </button>
  );
};

export default SendButton;
