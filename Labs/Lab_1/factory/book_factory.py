from Labs.Lab_1.domain.book import FictionBook, NonFictionBook

class BookFactory:
    @staticmethod
    def create_book(genre, title, author, isbn, publish_year):
        if genre.lower() == "fiction":
            return FictionBook(title, author, isbn, publish_year)
        elif genre.lower() == "non-fiction":
            return NonFictionBook(title, author, isbn, publish_year)
        else:
            raise ValueError("Unknown book genre")
