import React, { useState } from 'react';

const Flashcard = ({}) => {
  const images = [];
  for (let i = 1; i <= 144; i++) {
  images.push(`pdftoimage/output_images/image${i}.jpg`);
  }
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);

  const handleNextImage = () => {
    const randomIndex = Math.floor(Math.random() * images.length);
    setCurrentImageIndex(randomIndex);
    setRevealed(false);
  };

  const handleReveal = () => {
    setRevealed(true);
  };

  return (
    <div>
      <div style={{ position: 'relative' }}>
        <img src={images[currentImageIndex]} alt="Flashcard" />
        {!revealed && (
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '35%',
              backgroundColor: 'white',
              
            }}
          />
        )}
      </div>
      {!revealed && <button onClick={handleReveal}>Reveal</button>}
      <button onClick={handleNextImage}>Next</button>
    </div>
  );
};

export default Flashcard;