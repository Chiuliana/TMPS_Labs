from Labs.Lab_1.singleton.library_singleton import Library
from Labs.Lab_1.factory.book_factory import BookFactory
from Labs.Lab_1.builder.user_builder import UserBuilder
from Labs.Lab_1.decorator.book_decorator import BestSellerDecorator, NewArrivalDecorator
from Labs.Lab_1.adapter.book_adapter import BookAdapter, OldBookFormat
from Labs.Lab_1.domain.book import FictionBook, NonFictionBook

def main():
    # Access the singleton instance of the Library
    library = Library()

    # Use the Factory Method to create books with different genres
    print("Creating books using Factory Method:")
    book1 = BookFactory.create_book("Fiction", "1984", "George Orwell", "123456789")
    library.add_book(book1)

    book2 = BookFactory.create_book("Non-Fiction", "Sapiens", "Yuval Noah Harari", "987654321")
    library.add_book(book2)

    # Use the Builder pattern to create a user with optional fields
    print("\nCreating a user using Builder Pattern:")
    user_builder = UserBuilder()
    user = user_builder.set_name("Alice").set_user_id("U001").build()
    library.add_user(user)

    # Using Decorator Pattern to decorate books
    print("\nDecorating books using Decorator Pattern:")
    best_seller_book = BestSellerDecorator(book1)
    new_arrival_book = NewArrivalDecorator(book2)
    library.add_book(best_seller_book)
    library.add_book(new_arrival_book)

    # Show library status
    print("\nLibrary Status:")
    print(library)

    # Using Adapter Pattern to adapt old book format
    print("\nUsing Adapter Pattern to adapt an old book format:")
    old_book = OldBookFormat("The Old Man and the Sea", "Ernest Hemingway", "54321", 1952)
    adapted_book = BookAdapter(old_book)
    print(adapted_book)  # This will output the adapted book in the new format

if __name__ == "__main__":
    main()
