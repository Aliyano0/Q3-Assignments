def get_first_elem(lst):
  print(lst[0])

def get_lst():
  lst: list = []
  elem: str = input("Please enter an element of the list or press enter to stop: ")

  while elem != "":
    lst.append(elem)
    elem: str = input("Please enter an element of the list or press enter to stop: ")
  return lst


def main():
    lst = get_lst()
    get_first_elem(lst)


if __name__ == '__main__':
    main()