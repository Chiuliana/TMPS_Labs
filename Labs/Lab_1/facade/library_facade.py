from Labs.Lab_1.domain.user import User
from Labs.Lab_1.factory.book_factory import BookFactory
class LibraryFacade:
    def __init__(self):
        self.books = []
        self.users = []
        self.sort_strategy = None  # Initially no sorting strategy

    def add_book(self, genre, title, author, isbn, publish_year):
        book = BookFactory.create_book(genre, title, author, isbn, publish_year)
        self.books.append(book)
        print(f"Book added: {book}")

    def register_user(self, name, user_id):
        user = User(name, user_id)  # Assuming you have a User class
        self.users.append(user)
        print(f"User registered: {user}")

    def show_books(self):
        for book in self.books:
            print(book)

    def show_users(self):
        for user in self.users:
            print(user)

    def show_library_status(self):
        print(f"Library has {len(self.books)} books and {len(self.users)} users.")

    def decorate_book_as_best_seller(self, title):
        for book in self.books:
            if book.get_title() == title:
                book.decorate("Best Seller")
                print(f"Book decorated as Best Seller: {book}")

    def decorate_book_as_new_arrival(self, title):
        for book in self.books:
            if book.get_title() == title:
                book.decorate("New Arrival")
                print(f"Book decorated as New Arrival: {book}")

    def adapt_old_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                print(f"Adapted old book: Adapted Old Book: {book}")
                break

    def set_sort_strategy(self, strategy):
        self.sort_strategy = strategy

    def show_sorted_books(self):
        if self.sort_strategy:
            sorted_books = self.sort_strategy.sort(self.books)
            for book in sorted_books:
                print(book)
        else:
            print("No sorting strategy set!")
