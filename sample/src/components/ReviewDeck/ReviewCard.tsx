// ReviewCard.tsx
import React, { FC, useState } from 'react';

interface ReviewCardProps {
  question: string;
  answer: string;
  onMarkCorrect: () => void;
  onMarkIncorrect: () => void;
}

const ReviewCard: FC<ReviewCardProps> = ({ question, answer, onMarkCorrect, onMarkIncorrect }) => {
  const [showAnswer, setShowAnswer] = useState(false);
  
  const toggleAnswer = () => {
    setShowAnswer(!showAnswer);
  };

  return (
    <div className="review-card">
      <div className="card-content" onClick={toggleAnswer}>
        <p>{question}</p>
      </div>
    
      <div className="card-content">
        <h3>Answer</h3>
        <p>{answer}</p>
        <div>
          <button onClick={onMarkCorrect}>Mark as Correct</button>
          <button onClick={onMarkIncorrect}>Mark as Incorrect</button>
        </div>
      </div>
    </div>
  );
};

export default ReviewCard;
