from Labs.Lab_1.domain.book import Book

class BookSortStrategy:
    def sort(self, books):
        pass

class SortByTitle(BookSortStrategy):
    def sort(self, books):
        return sorted(books, key=lambda book: book.title)  # Directly access 'title'

class SortByAuthor(BookSortStrategy):
    def sort(self, books):
        return sorted(books, key=lambda book: book.author)  # Directly access 'author'

class SortByPublishYear(BookSortStrategy):
    def sort(self, books):
        return sorted(books, key=lambda book: book.publish_year)  # Directly access 'publish_year'
