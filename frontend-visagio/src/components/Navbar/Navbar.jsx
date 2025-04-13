import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import "./Navbar.css";

const Navbar = () => {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="home-buttons">
      <button
        onClick={() => navigate('/colaborador')}
        className={`btn-colaborador ${(location.pathname === '/colaborador' || location.pathname === '/') ? 'active' : ''}`}
      >
        Colaborador
      </button>
      <button
        onClick={() => navigate('/socio')}
        className={`btn-socio ${location.pathname === '/socio' ? 'active' : ''}`}
      >
        Sócio
      </button>
    </div>
  );
};

export default Navbar;
