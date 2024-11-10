# Laboratory Work No.2 Structural Design Patterns

### Course: TMPS
### Author: Chichioi Iuliana, FAF-221

----

## Objectives


__1. Study and understand the Structural Design Patterns.__

__2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.__

__3. Implement some additional functionalities using structural design patterns.__

---

## Some Theory:


Structural Design Patterns focus on how objects and classes are composed to form larger structures while keeping these structures flexible and efficient. The main aim of structural patterns is to ease the creation of large and complex systems by simplifying relationships and making the system components work together.

### Types of Structural Design Patterns

- **Adapter Pattern**: Allows incompatible interfaces to work together.
- **Builder Pattern**: Helps in constructing complex objects step by step.
- **Decorator Pattern**: Adds additional functionalities to an object dynamically.

In this lab, I implemented three structural design patterns to enhance a Library Management System, allowing users to add books, manage users, and enhance existing functionalities dynamically and efficiently.

---

## Main tasks:
__1. By extending your project, implement atleast 3 structural design patterns in your project.__

__2. Keep your files grouped (into packages/directories) by their responsibilities (an example project structure).__

__3.  Document your work in a separate markdown file according to the requirements presented below (the structure can be extended of course).__


---

## Domain Choice: Library Management System

The domain selected for this implementation is a **Library Management System**, where the aim is to manage books, users, and their interactions. The system will provide functionalities such as book registration, user registration, and dynamic updates to book information.

---

## Project Structure

```
Labs
└── Lab_1
    ├── adapter
    │   └── book_adapter.py
    ├── builder
    │   └── user_builder.py
    ├── decorator
    │   └── book_decorator.py
    ├── domain
    │   ├── book.py
    │   ├── librarian.py
    │   └── user.py
    ├── facade
    │   └── library_facade.py
    ├── factory
    │   └── book_factory.py
    ├── models
    │   └── book_models.py
    ├── singleton
    │   └── library_singleton.py
    ├── utilities
    │   └── library_utils.py
    ├── client.py
```

---

## Implementation Description & Explanation

This project demonstrates the use of **Structural Design Patterns—Adapter, Builder, and Decorator**—within a **Library Management System**.

These patterns are designed to make the system more flexible, modular, and easily extendable.

### 1.Adapter Pattern for Book Format Conversion

I implemented the **Adapter Pattern** to allow compatibility between different book formats. The idea was to integrate a legacy `OldBookFormat` with a new system that required a specific book format.

**Why Adapter?** 

The **Adapter Pattern** is useful here to convert the interface of an old book format into the interface required by the new system. This allows us to reuse the old `OldBookFormat` class without modifying it while still working with the new system.

**Code Snippet:**

```python

class OldBookFormat:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

class BookAdapter:
    def __init__(self, old_book):
        self.title = old_book.title
        self.author = old_book.author
        self.isbn = old_book.isbn
        self.year = old_book.year
        self.format = "New Book Format"

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.format}"

```
**How It Works**

The **OldBookFormat** represents the legacy format that needs to be adapted. The `BookAdapter` takes an instance of `OldBookFormat` and converts it into a form compatible with the new system.

The adapter adds a new `format` property to identify that the book is now in the "New Book Format".

This pattern allows the system to work with older formats without needing to modify the legacy code.

---

### 2.Facade Pattern

The **Facade Pattern** simplifies interactions with the complex **Library system**. By providing a single interface for adding books, users, and decorations, this pattern hides the complexities of the underlying components and presents a clean, easy-to-use API.

**Why Facade?** 

The **Facade Pattern** streamlines the process of managing books and users, abstracting the internal complexity of the **Library system** and presenting a simple interface for users to interact with.

**Code Snippet:**

```python
# facade/library_facade.py
class LibraryFacade:
    def __init__(self):
        self.library = Library()

    def add_book(self, genre, title, author, isbn):
        book = BookFactory.create_book(genre, title, author, isbn)
        self.library.add_book(book)
        print(f"Book added: {book}")

    def register_user(self, name, user_id):
        user_builder = UserBuilder()
        user = user_builder.set_name(name).set_user_id(user_id).build()
        self.library.add_user(user)
        print(f"User registered: {user}")

    def show_library(self):
        print(self.library)
```
**How It Works**

- The `Library` class serves as the facade, exposing simple methods like `add_book` and `add_user` to interact with the internal components of the system.
- The user does not need to deal with the intricacies of the book factory, user builder, or decorators, making the code easy to use.

This pattern allows the client to interact with the system more easily, without needing to understand the underlying details.

---

### 3.Decorator Pattern for Book Enhancements

I applied the **Decorator Pattern** to dynamically add additional features to books, such as marking them as `Best Seller` or `New Arrival`. This pattern allows adding responsibilities to an object without modifying its core structure.

**Why Decorator?**

The **Decorator Pattern** allows us to enhance the `Book` object with new functionalities dynamically. By using decorators, we can apply multiple features (like `Best Seller` or `New Arrival`) without altering the core book logic.

**Code Snippet:**

```python
# decorator/book_decorator.py

class BookDecorator:
    def __init__(self, book):
        self.book = book

class BestSellerDecorator(BookDecorator):
    def __str__(self):
        return f"{self.book} - Best Seller!"

class NewArrivalDecorator(BookDecorator):
    def __str__(self):
        return f"{self.book} - New Arrival!"

```
**How It Works**

- The `BookDecorator` class serves as a base class for all decorators. It contains a reference to the book object that it decorates.
- The `BestSellerDecorator` and `NewArrivalDecorator` add additional functionality to the book, such as appending a label like "Best Seller" or "New Arrival" when the book is printed.

This pattern allows for flexible, dynamic enhancements to objects without changing their core logic.

---
### 4.Main Application - `client.py`

The `client.py` file showcases the implementation and usage of multiple design patterns—**Singleton, Factory Method, Builder, Decorator, and Adapter**—within a library management system.

- **Decorator Pattern**

The `BestSellerDecorator` and `NewArrivalDecorator` are used to dynamically enhance the functionality of books. These decorators add labels like "Best Seller" or "New Arrival" to books without changing the core logic of the `Book` class.

- **Adapter Pattern**

The `BookAdapter` adapts the old book format (`OldBookFormat`) into a new system-compatible format. This allows legacy data to be used without modifying the old book class, making the system more adaptable to future changes.

- **Facade Pattern**

The `LibraryFacade` class provides a simplified interface to interact with the library system. It exposes high-level methods like `add_book()`, `register_user()`, and `show_library()` while hiding the complexities of interacting with the underlying classes like `BookFactory`, `UserBuilder`, and `Library`. This simplifies the client's interaction with the system.

**Code Snippet:**

```python
#client.py
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

```
**How It Works**

The `main()` function demonstrates the practical application of these patterns. It begins by accessing the singleton instance of `Library`, then creates books using the factory method and adds them to the library. Next, a user is created using the builder pattern and added to the library as well.

Books are decorated using the decorator pattern, adding features like "Best Seller" and "New Arrival." The `LibraryFacade` is used to streamline interactions with the system, and an old book format is adapted to the new system format using the adapter pattern.

This approach showcases how various structural design patterns can be effectively applied together to create a flexible, scalable, and maintainable system.

---

## Conclusions

In this laboratory work, I implemented and explored **Structural Design Patterns** in a **Library Management System**. The patterns used were **Adapter**, **Facade**, and **Decorator**, which enhanced the system's flexibility, scalability, and maintainability.

### 1. **Adapter Pattern**
The **Adapter** pattern was used to integrate an old book format with the new system. It allowed legacy components to be reused without modification, improving compatibility and flexibility.

### 2. **Facade Pattern**
The **Facade** pattern simplified interactions with the system by providing a clean, unified interface to complex internal components, making the system easier to use.

### 3. **Decorator Pattern**
The **Decorator** pattern enabled dynamic enhancements to book objects, such as adding "Best Seller" or "New Arrival" labels, without altering the core book class, promoting flexibility and reusability.

### Overall Insights
- These patterns improved the system’s modularity and maintainability.
- They addressed issues of complexity and reusability, demonstrating how design patterns can simplify software architecture.
- The work reinforced the importance of using structural design patterns to build scalable and maintainable systems.

These patterns will be useful in future projects, where flexibility, reusability, and maintainability are key.



