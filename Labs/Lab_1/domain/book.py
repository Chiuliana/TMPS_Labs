class Book:
    def __init__(self, genre, title, author, isbn, publish_year):
        self.genre = genre
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publish_year = publish_year
        self.decorations = []

    def get_title(self):
        return self.title

    def decorate(self, decoration):
        self.decorations.append(decoration)

    def __str__(self):
        return f"[{self.genre}] '{self.title}' by {self.author} (ISBN: {self.isbn}, Year: {self.publish_year})" + \
               (f" Decorations: {', '.join(self.decorations)}" if self.decorations else "")

# FictionBook (specific book type)
class FictionBook(Book):
    def __init__(self, title, author, isbn, publish_year):
        super().__init__("Fiction", title, author, isbn, publish_year)

# NonFictionBook (specific book type)
class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publish_year):
        super().__init__("Non-Fiction", title, author, isbn, publish_year)
