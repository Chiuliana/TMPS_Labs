# Laboratory Work No.1 Creational Design Patterns

### Course: TMPS
### Author: Chichioi Iuliana, FAF-221

----

## Objectives


__1. Study and understand the Creational Design Patterns.__

__2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.__

__3. Use some creational design patterns for object instantiation in a sample project.__

---

## Some Theory:
In software engineering, **Creational Design Patterns** provide solutions for object creation, helping to manage object lifecycle efficiently. These patterns offer ways to create objects without directly instantiating classes, making the design more flexible and scalable. Key patterns include:
Some examples of this kind of design patterns are:

   * **Singleton :** Ensures that a class has only one instance and provides a global access point to it.
   * **Factory Method :** Provides an interface for creating objects in a superclass but allows subclasses to change the type of objects created.
   * **Builder :** Allows step-by-step construction of complex objects, enabling flexible instantiation with optional attributes.

---

## Main tasks:
__1. Choose an OO programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed).__

__2. Select a domain area for the sample project.__

__3. Define the main involved classes and think about what instantiation mechanisms are needed.__

__4. Based on the previous point, implement atleast 3 creational design patterns in your project.__

---

## Domain Choice: Library Management System

The **Library Management System** is an ideal domain for demonstrating Creational Design Patterns, with core entities like `Library`, `Book`, and `User`. This domain supports:

- **Singleton**: Ensures a single `Library` instance.
- **Factory Method**: Creates genre-specific `Book` objects.
- **Builder**: Constructs `User` objects with optional attributes.

This structured setup provides a clear, practical context for applying and understanding object creation patterns effectively.

---

## Project Structure

```
Labs
└── Lab_1
    ├── builder
    │   └── user_builder.py
    ├── domain
    │   ├── book.py
    │   ├── librarian.py
    │   └── user.py
    ├── factory
    │   └── book_factory.py
    ├── singleton
    │   └── library_singleton.py
    ├── client.py
```

---

## Implementation Description

This project demonstrates the use of **Creational Design Patterns—Singleton, Factory Method, and Builder**—within a Library Management System.

Below is a step-by-step description of each pattern's implementation and the rationale behind each decision.

### 1. Singleton Pattern for `Library` Class

I implemented the **Singleton pattern** for the `Library` class to ensure there is only one instance of the library in the system. This pattern is useful in managing resources that need to be accessed globally by different parts of the program.

**Why Singleton?** 

The library instance should be unique and accessible from anywhere, ensuring that `books` and `users` are managed in a single, centralized object.

**Code Snippet:**

```python
# singleton/library_singleton.py

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.users = []
        return cls._instance

```
**How It Works**

- The `Library` class overrides the `__new__` method, which checks if an instance already exists.
- If `_instance` is `None`, it creates a new instance; otherwise, it returns the existing one.
- This approach ensures that only one `Library` instance is created, centralizing the management of books and users.

### 2.Factory Method Pattern for `Book` Creation

Next, I implemented the **Factory Method** pattern in the `BookFactory`class. This pattern helps create different types of `Book` objects based on their genre, providing flexibility and future scalability.

**Why Factory Method?** 

The **Factory Method** allows adding new genres without modifying the core logic, making it easy to extend the application.

**Code Snippet:**

```python
# factory/book_factory.py
from domain.book import FictionBook, NonFictionBook

class BookFactory:
    @staticmethod
    def create_book(genre, title, author, isbn):
        if genre.lower() == "fiction":
            return FictionBook(title, author, isbn)
        elif genre.lower() == "non-fiction":
            return NonFictionBook(title, author, isbn)
        else:
            raise ValueError("Unknown genre")
```
**How It Works**
- `create_book` is a static method that takes a `genre` parameter and returns the appropriate `Book` subclass (either `FictionBook` or `NonFictionBook`).
- This approach separates the book creation logic from the rest of the application, allowing for easy addition of new genres if needed.

### 3.Builder Pattern for User Creation

I used the Builder pattern for creating `User` objects, which may include optional attributes. The builder pattern allows step-by-step construction of a `Use`r object, making it ideal for objects with optional fields.

**Why Factory Method?** 

The Builder pattern is ideal for `User` since not all attributes are mandatory. This pattern makes the code flexible and readable, enabling incremental setup of the `User` object.

**Code Snippet:**

```python
# builder/user_builder.py
from domain.user import User

class UserBuilder:
    def __init__(self):
        self.name = None
        self.user_id = None

    def set_name(self, name):
        self.name = name
        return self

    def set_user_id(self, user_id):
        self.user_id = user_id
        return self

    def build(self):
        return User(self.name, self.user_id)
```
**How It Works**

- `UserBuilder` has methods to set optional attributes (`name` and `user_id`) for a `User` object.
- The `build` method constructs the `User` instance once all desired attributes are set.
- This pattern allows flexible and readable user creation without requiring all fields to be specified.

### 4.Main Application - `client.py`

Finally, I created `client.py` as the main entry point. Here, I use the **Singleton pattern** to access the `Library` instance, the **Factory Method** to create `Book` objects, and the **Builder** to create `User` objects.


**Code Snippet:**

```python
# client.py
from singleton.library_singleton import Library
from factory.book_factory import BookFactory
from builder.user_builder import UserBuilder

def main():
    library = Library()

    book1 = BookFactory.create_book("Fiction", "1984", "George Orwell", "123456789")
    library.add_book(book1)

    user = UserBuilder().set_name("Alice").set_user_id("U001").build()
    library.add_user(user)

    print("\nLibrary Status:")
    print(library)

if __name__ == "__main__":
    main()
```
**How It Works**

- This script initializes the `Library` instance, adds books and users, and displays the library’s status.
- `BookFactory` and `UserBuilder` simplify the creation of `Book` and `User` objects, demonstrating how each pattern enhances modularity and flexibility.

---

## Conclusions

In this project, the **Library Management System** effectively incorporates the **Singleton, Factory Method, and Builder design patterns**, each addressing distinct needs in object creation. 

The **Singleton** pattern ensures that only one instance of the `Library` exists, centralizing data management. 

The **Factory Method** pattern allows for the creation of genre-specific `Book` objects, facilitating easy expansion of the system with new types. 

Meanwhile, the **Builder** pattern enhances flexibility by enabling the construction of `User` objects with optional fields. 

This structured approach to object creation has improved the code's modularity, readability, and scalability, successfully fulfilling all lab requirements.


