# Laboratory Work No.3 Behavioral Design Patterns

### Course: TMPS
### Author: Chichioi Iuliana, FAF-221

----

## Objectives


__1. Study and understand the Behavioral Design Patterns.__

__2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.__

__3. Implement some additional functionalities using behavioral design patterns.__

---

## Some Theory:


Behavioral Design Patterns focus on the interactions and responsibilities between objects, aiming to improve communication and reduce coupling. These patterns help organize workflows and make the system more adaptable and easier to maintain.

### Types of Behavioral Design Patterns

- **Strategy Pattern**: Allows for the definition of a family of algorithms and lets the algorithm be selected at runtime.
- **Observer Pattern**: Enables one-to-many dependency updates between objects.
- **Command Pattern**: Encapsulates requests as objects, allowing them to be logged, queued, or executed later.

In this lab, I used the **Strategy Pattern** to enable flexible sorting of books in a **Library Management System**.

---

## Main tasks:
__1. Extend the Library Management System to include functionalities that rely on behavioral design patterns.__

__2. Organize the project files into appropriate directories based on responsibilities.__

__3. ocument the work in a markdown file.__


---

## Domain Choice: Library Management System

The chosen domain is a **Library Management System**, where behavioral design patterns are used to enhance functionality, including sorting books, notifying users of new arrivals, and managing user actions like borrowing and returning books.

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
    │   ├── strategy
    │   │   └── book_sort_strategy.py
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

This project demonstrates the use of the **Strategy Pattern** within a **Library Management System**. The pattern is used to dynamically select a sorting algorithm for books based on user preference.

**Why Strategy Pattern?** 

The **Strategy Pattern** provides flexibility by allowing the sorting logic to be selected dynamically at runtime. Instead of hardcoding multiple sorting methods, the pattern enables clean encapsulation of algorithms, promoting code reusability and maintainability.


**Code Snippet:**

```python
# strategy/book_sort_strategy.py
class SortByTitle:
    def sort(self, books):
        return sorted(books, key=lambda book: book["title"])

class SortByAuthor:
    def sort(self, books):
        return sorted(books, key=lambda book: book["author"])

class SortByYear:
    def sort(self, books):
        return sorted(books, key=lambda book: book["year"])

```
**How It Works**

- **Encapsulation of Sorting Algorithms:**  
  Each sorting strategy (e.g., sorting by title, author, or year) is encapsulated in a separate class. These classes implement a `sort` method, which defines the logic for that particular strategy.

- **Dynamic Selection of Strategy:**  
  The client code does not need to know the implementation details of the sorting strategies. It simply chooses the desired strategy class (e.g., `SortByTitle`, `SortByAuthor`, or `SortByYear`) and calls the `sort` method.

- **Flexibility and Extensibility:**  
  If a new sorting criterion (e.g., by genre) needs to be added, it can be done by creating a new class without modifying the existing code. This makes the system flexible and easily extensible.

---


---
### Main Application - `client.py`

The `client.py` serves as the entry point for the **Library Management System**. It utilizes multiple design patterns, including **Facade**, **Decorator**, **Adapter**, and **Strategy**, to showcase dynamic and user-friendly library management features.

---

### Functionality Overview

The program offers an interactive menu-driven system with the following options:

1. **Add a Book**  
   Users can add a book to the library by providing details such as title, author, genre, ISBN, and year of publication.  
   ```python
   genre = input("Enter book genre: ").strip()
   title = input("Enter book title: ").strip()
   library_facade.add_book(genre, title, author, isbn, publish_year)
   
   ```

2. **Register a User**  
   Allows registering a user with their name and user ID.
   ```python
   name = input("Enter user's name: ").strip()
   user_id = input("Enter user ID: ").strip()
   library_facade.register_user(name, user_id)

   ```
   
3. **Show Books/Users**  
   Displays all registered books and users through facade methods. 
   ```python
   library_facade.show_books()  # Displays all books
   library_facade.show_users()  # Displays all users

   ```

4. **Library Status**  
   Provides a summary of the library, including the number of books and users.
   ```python
   library_facade.show_library_status()

   ```

5. **Decorate a Book**  
   Dynamically decorates a book as "Best Seller" or "New Arrival" using the Decorator Pattern.
   ```python
   decoration = input("Select decoration: ")
   library_facade.decorate_book_as_best_seller(title)
   
   ```
6. **Adapt Old Book Format**  
   Integrates old book formats into the new system using the Adapter Pattern.
   ```python
   library_facade.adapt_old_book(title)

   ```
7. **Sort Books**  
   Dynamically sorts books by title, author, or year using the Strategy Pattern.
   ```python
   library_facade.set_sort_strategy(SortByTitle())
   library_facade.show_sorted_books()

   ```
8. **Exit**  
   Exits the application.

---

## Conclusions

In this laboratory work, I implemented and explored the **Behavioral Design Pattern—Strategy**—within a **Library Management System**. The **Strategy Pattern** provided flexible sorting strategies for books, such as sorting by title, author, or publication year.

### **Strategy Pattern**
The pattern allowed dynamic selection of sorting algorithms at runtime without altering the core logic. By encapsulating sorting behaviors into separate classes, the system became more maintainable and adhered to clean coding principles.

### Key Insights
- Improved adaptability by enabling flexible, runtime behavior changes.
- Enhanced modularity and maintainability through separation of concerns.
- Highlighted the power of behavioral patterns in creating scalable and dynamic systems.

This work reinforces the utility of behavioral patterns for projects requiring runtime flexibility and algorithm customization.



