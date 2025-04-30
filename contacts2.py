contacts = []

def contact_exists(name):
    return any(contact['name'].lower() == name.lower() for contact in contacts)

def add_contact():
    name = input("Enter the contact's name: ").strip()
    if contact_exists(name):
        print("This contact already exists.")
        return
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added successfully.")

def show_contacts():
    if not contacts:
        print("No contacts registered.")
        return
    print("\nCurrent contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def find_contact():
    name = input("Enter the name to search: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            field = input("Enter the field to update (phone/email): ").strip().lower()
            if field not in ["phone", "email"]:
                print("Invalid field. Only 'phone' or 'email' are allowed.")
                return
            new_value = input(f"Enter the new {field}: ").strip()
            contact[field] = new_value
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")
