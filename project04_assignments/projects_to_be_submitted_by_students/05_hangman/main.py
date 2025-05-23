import random
import string
from words import words

def get_valid_word(words):
  word: str = random.choice(words) 
  while '-' in word or ' ' in word:
    word = random.choice(words)
  word = word.upper()
  return word

def hangman():

  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  lives: int = 6


  while len(word_letters) > 0 and lives > 0:

    print(f"You have {lives} lives left and You have used these letters: ", ' '.join(used_letters))

    word_list = [letter if letter in used_letters else "-" for letter in word]

    print("Current word: ", ' '.join(word_list))


    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives = lives - 1
        print("Letter is not in word.")
    elif user_letter in used_letters:
      print("You have already used that character. Please try again. ")
    else: 
      print("Invalid character. Please try again")

  # outside the while loop
  if lives == 0:
    print(f"You died, sorry. The word was {word}.")
    
  else:
    print(f"You guessed the word {word}!!")


if __name__ == '__main__':
    hangman()