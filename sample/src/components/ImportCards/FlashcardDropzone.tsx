// FlashcardDropzone.tsx
import React, { FC, useState } from 'react';
import { Flashcard } from '../../types';
import Dropzone, { useDropzone } from 'react-dropzone';

// https://react-dropzone.js.org/#section-custom-validation
interface Props {
  onFileChange: (file: File) => void;
  flashcards: Flashcard[];
}

const FlashcardDropzone: FC<Props> = ({ onFileChange, flashcards }) => {
  const {getRootProps} = useDropzone({
    onDrop: files => console.log(files),
  })
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      onFileChange(file);
    }
  };

  return (
    <div>
      <label>Import CSV File:</label>
      <Dropzone>
      {({getRootProps, getInputProps}) => (
        <div {...getRootProps()} className='dropzone'>
          <input {...getInputProps()} />
          <p>Drag 'n' drop some files here, or click to select files</p>
        </div>
        )}
      </Dropzone>
      {flashcards.length > 0 && (
        <div className="flashcard-preview">
          <h2>Flashcard Preview:</h2>
          <ul>
            {flashcards.map((flashcard, index) => (
              <li key={index}>
                <strong>Question:</strong> {flashcard.question}, <strong>Answer:</strong>{' '}
                {flashcard.answer}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default FlashcardDropzone;
