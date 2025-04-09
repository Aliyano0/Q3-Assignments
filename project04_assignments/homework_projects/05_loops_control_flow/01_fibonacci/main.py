MAX_LENGTH: int = 10000 



def main():
  curr_num:int = 0
  next_term: int = 1
  while curr_num <= MAX_LENGTH:
    print(curr_num)
    num_after_next: int = curr_num + next_term
    curr_num = next_term
    next_term = num_after_next



if __name__ == '__main__':
  main()


