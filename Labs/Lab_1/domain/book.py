class Book:
    # Base class representing a book.

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class FictionBook(Book):
    # Represents a Fiction book.

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.genre = "Fiction"

    def __str__(self):
        return f"[Fiction] {super().__str__()}"


class NonFictionBook(Book):
    # Represents a Non-Fiction book.

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.genre = "Non-Fiction"

    def __str__(self):
        return f"[Non-Fiction] {super().__str__()}"
