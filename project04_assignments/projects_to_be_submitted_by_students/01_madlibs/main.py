
def main():
  adj: str = input("Adjective: ")
  verb1: str = input("Verb: ")
  verb2: str = input("Verb: ")
  famous_person: str = input("Famous person: ")

  madlib = f"Computer programming is so ${adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
  print(madlib)

if __name__ == "__main__":
  main()