def in_range(n, low, high):
  if n >= low and n <= high:   
    return True
    
  return False


def main():
  low: int = input("Enter low: ")
  n: int = input("Enter a number: ")
  high: int = input("Enter high: ")
  if in_range(n, low, high):
     print("True")
  else:
     print("False")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()