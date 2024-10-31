from Labs.Lab_1.singleton.library_singleton import Library
from Labs.Lab_1.factory.book_factory import BookFactory
from Labs.Lab_1.builder.user_builder import UserBuilder

def main():
    # Access the singleton instance of the Library
    library = Library()

    # Use the Factory Method to create books and add them to the library
    book1 = BookFactory.create_book("Fiction", "1984", "George Orwell", "123456789")
    library.add_book(book1)

    book2 = BookFactory.create_book("Non-Fiction", "Sapiens", "Yuval Noah Harari", "987654321")
    library.add_book(book2)

    # Use the Builder pattern to create a user with optional fields
    user_builder = UserBuilder()
    user = user_builder.set_name("Alice").set_user_id("U001").build()
    library.add_user(user)

    # Output the current state of the library
    print("\nLibrary Status:")
    print(library)

if __name__ == "__main__":
    main()
