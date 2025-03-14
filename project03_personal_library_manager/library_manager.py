import os
import json


DATA_FILE = "book_data.json"

##  ##  ## Function to load books from file ##  ##  ##
def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

books_list = load_books()

##  ##  ##  Function to save books to file  ##  ##  ## 
def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)


##  ##  ##  ##  Function to search book  ##  ##  ##
def search_book():
    while True:
        print("\n==== SEARCH BOOKS ====")
        print("1. Search by Title")
        print("2. Search by Author")
        print("0. Return to Main Menu")

        search_input = input("\nEnter your choice: ").strip()

        if search_input == "1":
            search_query = input("\nEnter part of the book title to search: ").strip().lower()

            # Filter matching books
            found_books = [
                book for book in books_list
                if search_query in book["title"].lower()
            ]

            if found_books:
                print(f"\nFound {len(found_books)} book(s):")
                for index, book in enumerate(found_books, 1):
                    print(f"\t{index}. {book['title']} by {book['author']} ({book['publish_year']}) - {book['genre']}, {book['is_read']}")
            else:
                print("\nNo books found with that title.")

        elif search_input == "2":
            search_query = input("\nEnter part of the author name to search: ").strip().lower()

            # Filter matching books
            found_books = [
                book for book in books_list
                if search_query in book["author"].lower()
            ]

            if found_books:
                print(f"\nFound {len(found_books)} book(s):")
                for index, book in enumerate(found_books, 1):
                    print(f"\t{index}. {book['title']} by {book['author']} ({book['publish_year']}) - {book['genre']}, {book['is_read']}")
            else:
                print("\nNo books found by that author.")

        elif search_input == "0":
            print("\nReturning to the main menu.")
            break

        else:
            print("\nPlease enter a valid option (1, 2, or 0).")



##  ##  ##  ##  Function to display statistics  ##  ##  ##
def display_statistics():
    print("\n==== BOOKS STATS ====")
    books_read = 0
    # Iterating the list to get read books quantity.
    for book in books_list:
        if book["is_read"] == "Read":
            books_read += 1
    books_quantity: int = len(books_list)
    #  Handle zero books case to avoid division by zero
    if books_quantity == 0:
        read_percentage = 0
    else:
        # Applied simple percentage formula
        read_percentage: int = (books_read / books_quantity) * 100
    print(f"""
Total books: {books_quantity}
Books read: {books_read}
Percentage read: {read_percentage:.2f}%
""")         



##  ##  ##  ##  Function to display all books  ##  ##  ##
def list_all_books():
    # Checking if the list isn't empty.
    if books_list:
        print(f"\n\tBooks quantity: {len(books_list)}")
        
        # Using enumerate to loop through the list and get the index
        for index, book in enumerate(books_list, start=1):
            print(f"\t\t{index}. {book['title']} by {book['author']} ({book['publish_year']}) - {book['genre']}, {book['is_read']}")
    
    # Error if the library is empty
    else:
        print("⚠ Library is empty. Add a book first!")



##  ##  ##  ##  Function to add a book  ##  ##  ##
def add_book():
    print("\n==== ADD A BOOK ====")
    title: str = input("Enter the Book Title: ")
    # Stripping whitespaces from left and right of the strings.
    title = title.strip()
    author: str = input("Enter Author's name: ")
    author = author.strip()
    # Getting a Publish year in int and implemented type checking.
    while True:    
        publish_year: int = input("Enter the Publication year: ")
        if publish_year.isdigit():
            break
        else: 
            print("Enter a valid year!")
    genre: str = input("Enter the Genre: ")
    genre = genre.strip()
    while True:
        read_status: str = input("Have you read this book? (yes/y OR no/n): ")
        is_read: str = "Unread"
        if read_status.lower() == "n" or read_status.lower == "no":
            is_read = "Unread"
            break
        elif read_status.lower() == "y" or read_status.lower() == "yes":
            is_read = "Read"
            break
        else:
            print("Enter a valid option!!")

    book_details:dict = {
            "title": title,
            "author": author,
            "publish_year": publish_year,
            "genre": genre,
            "is_read": is_read,
    }

    books_list.append(book_details)
    print(f"Book added successfully! {book_details["title"]}")
    print("New List is:")
    list_all_books()



##  ##  ##  ##  Function to remove a book  ##  ##  ##
def remove_book():
    print("\n==== REMOVE A BOOK ====")
    # Getting input to remove the book
    search_input: str = input("\nEnter the title of a book you want to remove: ")
    search_input = search_input.strip()
    # Iterating the list
    for book in books_list:
        # Checking if the input title is present in the list
        if book["title"] == search_input:
            # Removing the book from the list.
            books_list.remove(book)
            print("Book is removed! The new list of books is: ")
            list_all_books()
            # Eror if the input title is not present in the list.
        else:
            print("Book not found!")



##  ##  ##  ##  Library Initializer  ##  ##  ##
def library():
    
    print("\n==== WELCOME TO YOUR PERSONAL LIBRARY MANAGER! ====")
    while True:
        print("""
1. Add a book.
2. Remove a book.
3. Search for a book.
4. Display all books.
5. Display statistics.
6. Exit
              """)
        
        user_input = input("Enter your choice: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                add_book()
            elif user_input == 2:
                remove_book()
            elif user_input == 3:
                search_book()
            elif user_input==4:
                list_all_books()
            elif user_input == 5:
                display_statistics()
            elif user_input == 6:
                save_books(books_list)
                break    
            else: 
                print("\nEnter a valid option!")
        else:
            print("\nEnter a valid option!")


library()