import random
words = ["apple", "banana", "orange", "computer", "python", "programming"]
chosen_word = random.choice(words)
guessed = []
incorrect = 0
max = 5

hangman_stages = [
  """
      --------
      |      |
      |
      |
      |
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |
      |
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |      |
      |
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |     /|\
      |
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |     /|\
      |     /
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |     /|\
      |     / \
      |
    =========
  """,
  """
      --------
      |      |
      |      O
      |     /|\
      |     / \
      |    /   
    =========
  """
]

def display_game(word, incorrect, hangman_stage):
  print(hangman_stage[incorrect])
  print("Word: ", end="")
  for i in word:
    if i in guessed:
      print(i, end=" ")
    else:
      print("_", end=" ")
  print("\nIncorrect guesses:", incorrect, "/", max)
  print("Guessed letters:", guessed)

def get_guess():
  
  while True:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
    elif guess in guessed:
      print("You already guessed that letter. Try again.")
    else:
      return guess


def check_guess(word, guess):
  """Checks the guessed letter against the word and updates game state."""
  global guessed
  global incorrect
  guessed.append(guess)
  if guess in word:
    return True
  else:
    incorrect += 1
    return False


def play_again():
  choice = input("Play again? (y/n): ").lower()
  if choice == "y":
    global chosen_word, guessed, incorrect
    chosen_word = random.choice(words)
    guessed = []
    incorrect = 0
    return True
  else:
    return False


def main():
  print("Welcome to Hangman!")
  while True:
    word_to_guess = list(chosen_word)
    game_over = False

    while not game_over:
      display_game(word_to_guess, incorrect, hangman_stages)
      guess = get_guess()
      is_correct = check_guess(chosen_word, guess)

      if is_correct:
        # Check for win condition
        if all(letter in guessed for letter in chosen_word):
          display_game(word_to_guess, incorrect, hangman_stages)
          print("Congratulations! You guessed the word.")
          game_over = True
      else:
        # Check for loss condition
        if incorrect == max:
          display_game(word_to_guess, incorrect, hangman_stages)
          print("Sorry, you ran out of guesses. The word was:", chosen_word)
          game_over = True

    if not play_again():
      break


if __name__ == "__main__":
  main()
