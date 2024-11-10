from Labs.Lab_1.singleton.library_singleton import Library
from Labs.Lab_1.factory.book_factory import BookFactory
from Labs.Lab_1.builder.user_builder import UserBuilder

class LibraryFacade:
    def __init__(self):
        self.library = Library()

    def add_book(self, genre, title, author, isbn):
        book = BookFactory.create_book(genre, title, author, isbn)
        self.library.add_book(book)
        print(f"Book added: {book}")

    def register_user(self, name, user_id):
        user_builder = UserBuilder()
        user = user_builder.set_name(name).set_user_id(user_id).build()
        self.library.add_user(user)
        print(f"User registered: {user}")

    def show_library(self):
        print(self.library)
