// ReviewHeader.tsx
import React, { FC } from 'react';

interface ReviewHeaderProps {
  title: string;
}

const ReviewHeader: FC<ReviewHeaderProps> = ({ title }) => {
  return (
    <div className="review-header">
      <h2>{title}</h2>
    </div>
  );
};

export default ReviewHeader;
