from Labs.Lab_1.domain.book import FictionBook, NonFictionBook

class BookFactory:
    # Factory class to create Book instances based on genre.
    @staticmethod
    def create_book(genre, title, author, isbn):
        if genre.lower() == "fiction":
            print(f"Creating Fiction book: {title}")
            return FictionBook(title, author, isbn)
        elif genre.lower() == "non-fiction":
            print(f"Creating Non-Fiction book: {title}")
            return NonFictionBook(title, author, isbn)
        else:
            raise ValueError(f"Unknown genre '{genre}'. Please choose either 'Fiction' or 'Non-Fiction'.")
