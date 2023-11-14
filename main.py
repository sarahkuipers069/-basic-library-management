class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def borrow_book(self, book_id, member_id):
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                print(f"Member {member_id} has borrowed the book with ID {book_id}.")
                return
        print(f"The book with ID {book_id} is not available for borrowing.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.is_available = True
                print(f"The book with ID {book_id} has been returned.")
                return
        print(f"The book with ID {book_id} is not valid for return.")

if __name__ == "__main__":
    library = Library()
    library.add_book(Book(1, "The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book(3, "1984", "George Orwell"))

    library.display_available_books()

    library.borrow_book(2, 101)

    library.display_available_books()

    library.return_book(2)

    library.display_available_books()
