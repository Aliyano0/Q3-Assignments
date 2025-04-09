import random

def guess(x):  
  random_num: int = random.randint(1, x)
  guess: int = 0
  while guess != random_num:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_num:
      print("Sorry, guess again. Too low!")
    else:
      print("Sorry, guess again. Too high!")
  print(f"Yay, congrats. You have guessed the number {random_num} correctly!")

def main():
  guess(10)

if __name__ == "__main__":
  main()