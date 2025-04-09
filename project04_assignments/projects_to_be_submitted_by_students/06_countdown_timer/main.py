import time

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

  print("Timer completed!")


def main():
  t = input("Enter time in seconds: ")
  t = int(t)
  countdown(t)

if __name__ == "__main__":
  main()