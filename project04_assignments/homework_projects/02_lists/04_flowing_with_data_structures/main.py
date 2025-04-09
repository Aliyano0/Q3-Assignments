def add_three_copies(my_list, messsage):
  for i in range(3):
    my_list.append(messsage)


def main():
  messsage: str = input("Enter your message: ")
  my_list: list = []
  print("List before: ", my_list)
  add_three_copies(my_list, messsage)
  print("List after message: ", my_list)

  
if __name__ == "__main__":
    main()