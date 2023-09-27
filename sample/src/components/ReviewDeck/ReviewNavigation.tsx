// ReviewNavigation.tsx
import React, { FC } from 'react';

interface ReviewNavigationProps {
  onNext: () => void;
  onPrev: () => void;
}

const ReviewNavigation: FC<ReviewNavigationProps> = ({ onNext, onPrev }) => {
  return (
    <div className="review-navigation">
      <button onClick={onPrev}>Previous Card</button>
      <button onClick={onNext}>Next Card</button>
    </div>
  );
};

export default ReviewNavigation;
