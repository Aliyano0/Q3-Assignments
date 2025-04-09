import time


def main():
  for i in range(11):
    if i == 10:
      print("Liftoff!")
      break
    print(10-i)
    time.sleep(1.0)


if __name__ == '__main__':
  main()