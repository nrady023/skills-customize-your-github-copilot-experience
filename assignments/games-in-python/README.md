
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses string manipulation, loops, conditionals, and user input to let a player guess a hidden word.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a predefined list of words and randomly select one word for the player to guess.

#### Requirements
Completed program should:

- Define a list of possible words in the game.
- Use `random.choice()` to select a secret word.
- Initialize the game state to show underscores for each letter in the secret word.
- Track the number of remaining incorrect guesses.

### 🛠️ Player Guesses and Display Progress

#### Description
Allow the player to guess letters and update the display to show correct letters while hiding remaining letters.

#### Requirements
Completed program should:

- Accept single-letter guesses from the player.
- Reveal all matching letters in the current word display.
- Keep an updated list of correct and incorrect guesses.
- Show the current progress in `_ _ _` format after each guess.

### 🛠️ Win/Lose Logic

#### Description
End the game when the player either guesses the entire word or runs out of attempts, and display an appropriate message.

#### Requirements
Completed program should:

- End the game when the player has correctly guessed every letter.
- End the game when the player uses all allowed incorrect attempts.
- Display a win message if the player guesses the word.
- Display a lose message and reveal the correct word if the player runs out of attempts.
