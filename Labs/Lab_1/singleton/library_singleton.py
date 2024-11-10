class Library:
    # Represents the library managing books and users
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.users = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.users)} users."
