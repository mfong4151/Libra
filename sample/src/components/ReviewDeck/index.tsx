import react, {useState} from 'react';
import { useParams } from 'react-router-dom';
import ReviewCard from './ReviewCard';
interface Deck {
    name: string;
    cards: { question: string; answer: string }[];
  }

const decks: Deck[] = [
    // Define your decks and associated cards here
    {
      name: 'Deck 1',
      cards: [
        { question: 'Question 1', answer: 'Answer 1' },
        // Add more cards as needed
      ],
    },
    // Add more decks as needed
  ];
  


const ReviewDeck = () => {
    const params = useParams()
    const [selectedDeck, setSelectedDeck] = useState(decks[0].name);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [correctAnswers, setCorrectAnswers] = useState(0);
    const [incorrectAnswers, setIncorrectAnswers] = useState(0);
    const currentDeck = decks.find((deck) => deck.name === selectedDeck);
    const currentCard = currentDeck?.cards[currentIndex];
    const handleMarkCorrect = () => {
        setCorrectAnswers(correctAnswers + 1);
        // Move to the next card or end the review when all cards are reviewed
        if (currentIndex < currentDeck!.cards.length - 1) {
          setCurrentIndex(currentIndex + 1);
        } else {
          // You can implement an end-of-review logic here
          // E.g., Show a summary or message
        }
      };
    
      const handleMarkIncorrect = () => {
        setIncorrectAnswers(incorrectAnswers + 1);
        // Move to the next card or end the review when all cards are reviewed
        if (currentIndex < currentDeck!.cards.length - 1) {
          setCurrentIndex(currentIndex + 1);
        } else {
          // You can implement an end-of-review logic here
          // E.g., Show a summary or message
        }
      };


    return(

        <>
      {currentCard && (
        <ReviewCard
          question={currentCard.question}
          answer={currentCard.answer}
          onMarkCorrect={handleMarkCorrect}
          onMarkIncorrect={handleMarkIncorrect}
        />
      )}
        </>
        ) 
}


export default ReviewDeck;