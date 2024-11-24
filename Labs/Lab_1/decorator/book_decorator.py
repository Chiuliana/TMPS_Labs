from Labs.Lab_1.domain.book import Book

class BookDecorator(Book):
    def __init__(self, book: Book):
        self._book = book

    def __str__(self):
        return str(self._book)  # Delegate the string conversion to the base book object


class BestSellerDecorator(BookDecorator):
    def __init__(self, book: Book):
        super().__init__(book)

    def __str__(self):
        # Just append the 'Best Seller' label without re-adding genre info
        return f"{str(self._book)} - Best Seller!"


class NewArrivalDecorator(BookDecorator):
    def __init__(self, book: Book):
        super().__init__(book)

    def __str__(self):
        # Just append the 'New Arrival' label without re-adding genre info
        return f"{str(self._book)} - New Arrival!"
