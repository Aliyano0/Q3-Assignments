##  ##  ##  ##  Function to display all books  ##  ##  ##
books_list = []



##  ##  ##  ##  Function to search book  ##  ##  ##
def search_book():
    # Getting search option by the user.
    print("1. Search by Title.")
    print("2. Search by Author.")
    search_input: int = input("\nEnter your choice: ")

    # Added an additional input type check.
    if search_input.isdigit():
        # Checking if the user has entered option 1.
        if search_input == "1":
            # Getting search input
            search_query = input("\nSearch book by Name: ")
            # Looping through the List of Dictionaries.
            print("Search results: ")
            for book in books_list:
                # Checking if the search input is present in the library list.
                if book["title"] == search_query:
                    print(f"\t{book["title"]} by {book["author"]} ({book["publish_year"]}) - {book["genre"]}, {book["is_read"]}")
                # Throwing error if the search input is not present in the list.
                else:
                    print("Search results: ")
                    print("\nBook not found!")
        # Checking if the user has entered option 2.
        elif search_input == "2":
            # Getting search input
            search_query = input("\nSearch book by Author: ")
            # Looping through the List of Dictionaries.
            print("Search results: ")
            for book in books_list:
                # Checking if the search input is present in the library list.
                if book["author"] == search_query:
                    print(f"\t{book["title"]} by {book["author"]} ({book["publish_year"]}) - {book["genre"]}, {book["is_read"]}")
                # Throwing error if the search input is not present in the list.
                else:
                    print("Search results: ")
                    print("\nBook not found!")          
        # Throwing error if user has not entered the valid option.
        else:
            print("\nEnter a valid option!")
    # Throwing error if user has not entered the valid option.
    else:
        print("\nEnter a valid option!!!")



##  ##  ##  ##  Function to display statistics  ##  ##  ##
def display_statistics():
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
        print(f"Books quantity: {len(books_list)}")
        # Looping through the list to display the data
        for book in books_list:
            print(f"\t{book["title"]} by {book["author"]} ({book["publish_year"]}) - {book["genre"]}, {book["is_read"]}")
    # Error if the library is empty
    else:
        print("⚠ Library is empty. Add a book first!")



##  ##  ##  ##  Function to add a book  ##  ##  ##
def add_book():
    title: str = input("Enter the Book Title: ")
    author: str = input("Enter Author's name: ")
    # Getting a Publish year in int and implemented type checking.
    while True:    
        publish_year: int = input("Enter the Publication year: ")
        if publish_year.isdigit():
            break
        else: 
            print("Enter a valid year!")
    genre: str = input("Enter the Genre: ")
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
  # Getting input to remove the book
  search_input = input("\nEnter the title of a book you want to remove: ")
  # Iterating the list
  for book in books_list:
    # Checking if the input title is present in the list
    if book["title"] == search_input:
        # Removing the book from the list.
        books_list.remove(book)
        print("Book is removed! The new list of book is: ")
        list_all_books()
    # Eror if the input title is not present in the list.
    else:
        print("Book not found!")



##  ##  ##  ##  Library Initializer  ##  ##  ##
def library():
    
    print("\nWelcome to your Personal Library Manager!")
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
                print("Library saved to file. Goodbye!")
                break    
            else: 
                print("\nEnter a valid option!")
        else:
            print("\nEnter a valid option!")


library()