def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
      print(str(year) + " is a Leap year!")
    else:
      print("Not a leap year.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()