# flash-card
# Flashy - Flashcard Learning App

## Description
Flashy is a vocabulary learning app built with Tkinter, designed to help users memorize French vocabulary. The app displays French words on one side of a card, and users can reveal their English translations by flipping the card. Words that are correctly identified are removed from the list, while incorrect answers are shown again for further review.

## Features
- Displays French words and their English translations
- Users can mark a word as "right" or "wrong"
- Tracks words that need to be learned and saves progress in a CSV file
- User-friendly interface with interactive buttons for each answer

## Requirements
- Python 3.x
- Tkinter (usually pre-installed with Python)
- Pandas library for handling word data

## Files
- `main.py`: The main file that runs the flashcard app.
- `images/`: Contains images used for card visuals and button icons (e.g., card front, card back, right and wrong buttons).
- `words_to_learn.csv`: A CSV file where words that need further study are saved.
- `french_words.csv`: The initial list of French words and their English translations.

## Usage
1. Ensure that you have Python 3.x installed.
2. Install the required dependencies:
   ```bash
   pip install pandas
