def main():
    degrees_fahrenheit: str= input("Input temperature in farenheit: ")
    degrees_fahrenheit: float= float(degrees_fahrenheit)
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")


if __name__ == "__main__":
    main()
