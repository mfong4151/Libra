// ReviewCards.tsx
import React, { FC, useState } from 'react';
import { Link } from 'react-router-dom';

const SelectDeck: FC = () => {

  const decks: number[] = [1, 2, 3, 4,5 ]
  return ( 
    <div className="review-cards">
      <h1>Select Your Deck</h1>
      <ul className='fdc'>
        {decks.map((deck, idx) => 
          <li key={idx}><Link to={`/review/${deck}`}>{deck}</Link></li>
        
        )}

      </ul>
    </div>
  );
};

export default SelectDeck;
