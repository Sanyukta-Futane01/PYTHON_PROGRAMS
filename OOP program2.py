class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def add_member(self):
        name = input("Enter member name: ")
        self.members.append(Member(name))
        print("Member added successfully!")

    def lend_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for book in self.books:
            if book.title == title and not book.is_borrowed:
                for member in self.members:
                    if member.name == name:
                        book.is_borrowed = True
                        member.borrowed_books.append(book.title)
                        print("Book lent successfully!")
                        return
        print("Book not available or member not found.")

    def return_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for member in self.members:
            if member.name == name:
                if title in member.borrowed_books:
                    member.borrowed_books.remove(title)
                    for book in self.books:
                        if book.title == title:
                            book.is_borrowed = False
                    print("Book returned successfully!")
                    return
        print("Return failed.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} by {book.author} - {status}")


# Menu-driven system
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.add_member()
    elif choice == 3:
        library.lend_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        library.display_books()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")