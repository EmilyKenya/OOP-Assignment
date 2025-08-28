# Parent class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def read(self):
        return f"You start reading '{self.title}'."

# Child class: EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # MB

    # Polymorphism: override the read method
    def read(self):
        return f"You open the eBook '{self.title}' on your device. File size: {self.file_size}MB."

# Create objects
physical_book = Book("The Richest Man in Babylon", "George S. Clason", 144)
ebook = EBook("The Richest Man in Babylon", "George S. Clason", 144, 1.5)

# Test the methods
print(physical_book.description())
print(physical_book.read())

print(ebook.description())
print(ebook.read())
