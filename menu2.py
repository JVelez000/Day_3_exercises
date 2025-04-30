from contacts2 import add_contact, show_contacts, find_contact, update_contact, delete_contact, contacts

def display_menu():
    print("\nContact Agenda Menu:")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Find Contact by Name")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            if contacts:
                find_contact()
            else:
                print("No contacts to search.")
        elif choice == "4":
            if contacts:
                update_contact()
            else:
                print("No contacts to update.")
        elif choice == "5":
            if contacts:
                delete_contact()
            else:
                print("No contacts to delete.")
        elif choice == "6":
            print("Exiting the agenda.")
            break
        else:
            print("Invalid choice. Please try again.")
