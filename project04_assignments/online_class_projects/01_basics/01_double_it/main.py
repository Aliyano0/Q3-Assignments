MAX_VALUE: int = 100

def main():
  user_input: int = input("Enter a number: ")
  num = int(user_input)
  while int(num) < MAX_VALUE:
    num = num * 2
    print(num)


if __name__ == "__main__":
  main()