from Labs.Lab_1.domain.book import Book

class BookFactory:
    # Factory class to create Book instances based on genre

    @staticmethod
    def create_book(genre, title, author, isbn):
        # i will specify later adding genre-specific behavior
        print(f"Creating {genre} book: {title}")
        return Book(title, author, isbn)
