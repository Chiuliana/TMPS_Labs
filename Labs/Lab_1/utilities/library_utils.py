from Labs.Lab_1.domain.book import Book

def search_books_by_author(library, author_name):
    # This function will search books in the library by author name
    books_by_author = [book for book in library.books if book.author.lower() == author_name.lower()]
    return books_by_author

def print_books(books):
    for book in books:
        print(book)
