from Labs.Lab_1.domain.book import Book

class OldBookFormat:
    def __init__(self, title, author, isbn, publish_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publish_year = publish_year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_publish_year(self):
        return self.publish_year

class BookAdapter(Book):
    def __init__(self, old_book: OldBookFormat):
        self.title = old_book.get_title()
        self.author = old_book.get_author()
        self.isbn = old_book.get_isbn()

    def __str__(self):
        return f"Adapted Book: '{self.title}' by {self.author} (ISBN: {self.isbn})"
