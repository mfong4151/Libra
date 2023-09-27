// ImportCards.tsx
import React, { FC, useState } from 'react';
import ImportCardsForm from './ImportCardsForm';
import FlashcardDropzone from './FlashcardDropzone';
import { DeckInfo, Flashcard } from '../../types';


const ImportCards: FC = ({ }) => {
  const [deckInfo, setDeckInfo] = useState<DeckInfo>({
    title: '',
    description: '',
    category: '',
  });
  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);

  const handleTitleChange = (value: string) => {
    setDeckInfo({ ...deckInfo, title: value });
  };

  const handleDescriptionChange = (value: string) => {
    setDeckInfo({ ...deckInfo, description: value });
  };

  const handleCategoryChange = (value: string) => {
    setDeckInfo({ ...deckInfo, category: value });
  };

  const handleFileChange = (file: File) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      if (event.target) {
        const csvData = event.target.result as string;
        parseCSV(csvData);
      }
    };
    reader.readAsText(file);
  };

  const parseCSV = (csvData: string) => {
    const rows = csvData.split('\n');
    const parsedFlashcards: Flashcard[] = [];
  
    if (rows.length >= 2) {
      const questionRow = rows[0].split(',');
      const answerRow = rows[1].split(',');
  
      // Ensure that the question and answer rows have the same number of columns
      if (questionRow.length === answerRow.length) {
        for (let i = 0; i < questionRow.length; i++) {
          const question = questionRow[i].trim();
          const answer = answerRow[i].trim();
  
          if (question && answer) {
            // Add the flashcard to the parsedFlashcards array
            parsedFlashcards.push({ question, answer });
          }
        }
  
        // Update the state with the parsed flashcards
        setFlashcards(parsedFlashcards);
      } else {
        // Handle error: The number of columns in question and answer rows should match
        console.error('CSV format error: Number of columns in question and answer rows do not match.');
      }
    } else {
      // Handle error: Insufficient rows in the CSV
      console.error('CSV format error: Insufficient rows in the CSV.');
    }
  };
  

  const handleSubmit = () => {
    if (deckInfo.title && flashcards.length > 0) {

    }
  };

  return (
    <>
      <h1>Import Flashcards</h1>
        <ImportCardsForm
          deckInfo={deckInfo}
          onTitleChange={handleTitleChange}
          onDescriptionChange={handleDescriptionChange}
          onCategoryChange={handleCategoryChange}
          />
        <FlashcardDropzone onFileChange={handleFileChange} flashcards={flashcards} />
        <button onClick={handleSubmit} disabled={!deckInfo.title || flashcards.length === 0}>
          Import Flashcards
        </button>
    </>
      );
};

export default ImportCards;
