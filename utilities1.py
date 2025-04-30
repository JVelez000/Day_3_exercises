#len() devuelve el numero de xxx o la cantidad de xxx, el +1 genera una id nueva con un numero las alto al anterior
#f"{len(xxx) + 1:03}" el 03 genera un numero de 3 digitos rellenando a la izquierda con 0 hasta el 99
# f"xxx{valor numerico o texto}" deja insertar variables distintas

books = []

def book_exists(title,author,year_of_publication):
	return any(
		book.get("title") == title and 
		book.get("author") == author and 
		book.get("year_of_publication") == year_of_publication 
		for book in books
	)

def add_book():
	title = input("Enter the book title: ")
	author = input("Enter the author's name: ")
	year_of_publication = input("Enter the year of publication: ")

	if book_exists(title,author,year_of_publication):
		print("The book is already registered, please try again. ")
		return

	book = {
		"id": f"{len(books) + 1:03}",
		"title" : title,
		"author" : author,
		"year_of_publication" : year_of_publication
	}
	books.append(book)
	print("the book was registered succesfully")
	
def show_books():
	if not books:
		print("No registered books ")
		return
	print("\nCurrent books")
	for book in books:
		print(
			f"id: {book.get('id', 'N/A')}, "
			f"title: {book.get('title', 'N/A')}, "
			f"author: {book.get('author', 'N/A')}, "
			f"year_of_publication: {book.get('year_of_publication', 'N/A')}"
		)

def find_book_by_id():
	try:
			book_id = input("\nEnter the book ID to search it (001 - ∞)")
			for book in books:
				if book.get("id") == book_id:
					print("\nThe book was found")
					print(
						f"id: {book.get('id', 'N/A')}, "
						f"title: {book.get('title', 'N/A')}, "
						f"author: {book.get('author', 'N/A')}, "
						f"year_of_publication: {book.get('year_of_publication', 'N/A')}"
					)
					return
			print("The book was not found")
	except Exception as e:
		print(f"An error has ocurred: {e}")

def delete_book():
	show_books()
	try:
		book_id = (input("\nEnter the book id to delete it (001 - ∞)"))
		for book in books:
			if book["id"] == book_id:
				books.remove(book)
				print("The book has been deleted succesfully")
				return
		print("The book was not found")
	except ValueError:
		print("Invalid input. Please enter a valid id number")

def modify_book():
    show_books()
    try:
        book_id = input("\nEnter the book ID to make the modification: ")
        field = input("Enter the field to modify (title, author, year_of_publication): ").replace(" ", "_").lower()
        
        if field not in ["title", "author", "year_of_publication"]:
            print(f"Invalid field: {field}. Valid fields are title, author, and year_of_publication.")
            return
        
        new_value = input("Enter the new value: ")
        
        for book in books:
            if book["id"] == book_id:
                book[field] = new_value
                print(f"Field '{field}' was modified successfully.")
                return
        
        print("The book was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

