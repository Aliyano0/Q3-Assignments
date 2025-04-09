def print_multiple(message: str, repeats: int): 
   for i in range(repeats): 
      print(message)


def main():
   message: str = input("Please type a message: ")
   repeat_num: int = input("Enter a number of times to repeat your message: ")
   print_multiple(message, int(repeat_num))



if __name__ == '__main__':
    main()