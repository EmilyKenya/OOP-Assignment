# Book Class Project 📚

This project demonstrates the creation of a Python class representing a book, including physical and digital formats. It explores **object-oriented programming concepts** like **inheritance** and **polymorphism**.

## Features

- **Book Class**: Represents a physical book with attributes like `title`, `author`, and `pages`.
- **EBook Class**: Inherits from `Book` and adds a `file_size` attribute. Overrides the `read()` method to demonstrate polymorphism.
- **Methods**:
  - `description()`: Returns a brief description of the book.
  - `read()`: Simulates reading the book (differs for physical book and eBook).

## Example Usage

```python
# Creating a physical book
physical_book = Book("The Richest Man in Babylon", "George S. Clason", 144)
print(physical_book.description())
print(physical_book.read())

# Creating an eBook
ebook = EBook("The Richest Man in Babylon", "George S. Clason", 144, 1.5)
print(ebook.description())
print(ebook.read())
