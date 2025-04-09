def main():
  lst: list= []
  elem: str = input("Enter an element or press enter to print the list: ")
  while elem != "":
    lst.append(elem)
    elem: str = input("Enter an element or press enter to print the list: ")
  print("Here's the list: ", lst)


if __name__ == '__main__':
    main()