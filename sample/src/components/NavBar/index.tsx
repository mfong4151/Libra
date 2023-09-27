
import React, {FC} from 'react';
import './navbar.css'
import { Link } from 'react-router-dom';

const NavBar:FC = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/import">Import Cards</Link>
        </li>
        <li>
          <Link to="/select">Review Cards</Link>
        </li>
        <li>
          <Link to="/organize">Organize Cards</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
