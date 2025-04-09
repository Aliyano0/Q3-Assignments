import random


def computer_guess(x):
   low: int = 1
   high: int = x
   feedback: str = ""
   while feedback != "c":
      if low != high:
        guess = random.randint(low, high)
      else: 
        guess = low
      feedback = input(f"Is {guess} guess to high (H), too low (L), or correct (C)??").lower()
      if feedback == "h":
        high = guess - 1
      elif feedback == "l":
        low = guess + 1
   print(f"Yay! The computer guessed your number, {guess} correctly! ")


def main():
  computer_guess(100)

if __name__ == "__main__":
  main()