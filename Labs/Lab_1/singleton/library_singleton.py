class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = []
            cls._instance.users = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def get_books(self):
        return self.books

    def get_users(self):
        return self.users

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
