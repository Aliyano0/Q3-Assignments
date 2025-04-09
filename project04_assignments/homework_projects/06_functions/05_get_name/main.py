def get_name():
    name: str = input("Enter your name: ")
    return name

# There is no need to edit code beyond this point

def main():
    name = get_name() 
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()