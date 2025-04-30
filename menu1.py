from utilities1 import add_book, show_books, delete_book, modify_book, find_book_by_id

def display_menu():
    print("Menu:")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Delete Book")
    print("4. Modify Book")
    print("5. Find Book by ID")
    print("6. Exit")
    
def menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            modify_book()
        elif choice == "5":
            find_book_by_id()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")