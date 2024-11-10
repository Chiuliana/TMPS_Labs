from Labs.Lab_1.domain.book import Book

class BookModel:
    # A model representing a book with more detailed attributes for storage
    def __init__(self, title, author, isbn, genre, publish_date, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publish_date = publish_date
        self.pages = pages

    def __str__(self):
        return f"BookModel(title={self.title}, author={self.author}, isbn={self.isbn}, genre={self.genre}, publish_date={self.publish_date}, pages={self.pages})"


class FictionBookModel(BookModel):
    def __init__(self, title, author, isbn, publish_date, pages, sub_genre):
        super().__init__(title, author, isbn, "Fiction", publish_date, pages)
        self.sub_genre = sub_genre

    def __str__(self):
        return f"Fiction Book: {super().__str__()}, Sub-genre: {self.sub_genre}"


class NonFictionBookModel(BookModel):
    def __init__(self, title, author, isbn, publish_date, pages, subject):
        super().__init__(title, author, isbn, "Non-Fiction", publish_date, pages)
        self.subject = subject

    def __str__(self):
        return f"Non-Fiction Book: {super().__str__()}, Subject: {self.subject}"
