from Labs.Lab_1.domain.book import Book

class OldBookFormat:
    def __init__(self, book: Book):
        # Extract the necessary attributes from the Book object
        self.title = book.title
        self.author = book.author
        self.isbn = book.isbn
        self.publish_year = book.publish_year  # Ensure that Book has this attribute

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_publish_year(self):
        return self.publish_year

    def __str__(self):
        return f"Adapted Old Book: {self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.publish_year})"


class BookAdapter(Book):
    def __init__(self, old_book: OldBookFormat):
        # Use the attributes from the OldBookFormat to set up the adapted book
        self.title = old_book.get_title()
        self.author = old_book.get_author()
        self.isbn = old_book.get_isbn()
        self.publish_year = old_book.get_publish_year()  # If you want to adapt this attribute too

    def __str__(self):
        return f"Adapted Book: '{self.title}' by {self.author} (ISBN: {self.isbn}, Year: {self.publish_year})"
