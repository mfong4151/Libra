// ImportCardsForm.tsx
import React, { FC } from 'react';
import { DeckInfo } from '../../types';

interface ImportCardsFormProps {
  deckInfo: DeckInfo;
  onTitleChange: (value: string) => void;
  onDescriptionChange: (value: string) => void;
  onCategoryChange: (value: string) => void;
}

const ImportCardsForm: FC<ImportCardsFormProps> = ({
  deckInfo,
  onTitleChange,
  onDescriptionChange,
  onCategoryChange,
}) => {
  return (
    <form>
      <div>

        <label>Title:</label>
        <input type="text" value={deckInfo.title} onChange={(e) => onTitleChange(e.target.value)} />
      </div>
      <div>

      <label>Description:</label>
      <input
        type="text"
        value={deckInfo.description}
        onChange={(e) => onDescriptionChange(e.target.value)}
        />
      </div>
      <div>

      <label>Category:</label>
      <input
        type="text"
        value={deckInfo.category}
        onChange={(e) => onCategoryChange(e.target.value)}
        />
      </div>
    </form>
  );
};

export default ImportCardsForm;
