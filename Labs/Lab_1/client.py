# client.py
from Labs.Lab_1.facade.library_facade import LibraryFacade
from Labs.Lab_1.domain.strategy.book_sort_strategy import SortByTitle, SortByAuthor, SortByPublishYear

def main():
    library_facade = LibraryFacade()

    while True:
        print("Welcome to the Library System!")
        print("---------------------------------------------------------")
        print("Please choose an option:")
        print("1. Add a book")
        print("2. Register a user")
        print("3. Show all books")
        print("4. Show all users")
        print("5. View library status")
        print("6. Apply a Best Seller or New Arrival decoration")
        print("7. Adapt an old book format")
        print("8. Sort books")
        print("9. Exit")

        choice = int(input())

        if choice == 1:
            # Prompt user for book details
            genre = input("Enter book genre (Fiction/Non-Fiction): ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            publish_year = input("Enter book publish year: ").strip()

            # Add the book through the library facade
            library_facade.add_book(genre, title, author, isbn, publish_year)

        elif choice == 2:
            # Register a user
            name = input("Enter user's name: ").strip()
            user_id = input("Enter user ID: ").strip()
            library_facade.register_user(name, user_id)

        elif choice == 3:
            # Show all books
            library_facade.show_books()

        elif choice == 4:
            # Show all users
            library_facade.show_users()

        elif choice == 5:
            # View library status
            library_facade.show_library_status()

        elif choice == 6:
            # Apply decoration
            title = input("Enter the book title to decorate: ").strip()
            decoration = input("Select decoration (Best Seller / New Arrival): ").strip()
            if decoration.lower() == "best seller":
                library_facade.decorate_book_as_best_seller(title)
            elif decoration.lower() == "new arrival":
                library_facade.decorate_book_as_new_arrival(title)
            else:
                print("Invalid decoration choice.")

        elif choice == 7:
            # Adapt an old book format
            title = input("Enter the old book title to adapt: ").strip()
            library_facade.adapt_old_book(title)

        elif choice == 8:
            # Sort books
            print("Choose a sorting option:")
            print("1. Sort by Title")
            print("2. Sort by Author")
            print("3. Sort by Publish Year")
            sort_choice = int(input())

            if sort_choice == 1:
                library_facade.set_sort_strategy(SortByTitle())
            elif sort_choice == 2:
                library_facade.set_sort_strategy(SortByAuthor())
            elif sort_choice == 3:
                library_facade.set_sort_strategy(SortByPublishYear())
            else:
                print("Invalid sorting option.")
                continue

            library_facade.show_sorted_books()

        elif choice == 9:
            print("Exiting the system...")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
