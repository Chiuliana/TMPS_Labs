from Labs.Lab_1.singleton.library_singleton import Library
from Labs.Lab_1.domain.book import Book
from Labs.Lab_1.domain.user import User

class Librarian:
    # Class for managing library actions by adding books and registering users.

    def __init__(self):
        self.library = Library()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.library.add_book(book)
        print(f"Added book: {book}")

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.library.add_user(user)
        print(f"Registered user: {user}")
