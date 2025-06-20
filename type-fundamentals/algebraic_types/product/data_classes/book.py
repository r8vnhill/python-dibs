"""
book.py – Minimal example showcasing Python dataclasses.

This script demonstrates the use of the `@dataclass` decorator to define a simple immutable
record-like structure in Python.
It creates an instance of the `Book` class, illustrates how to access its fields, print its string
representations, and perform equality checks.

## Usage

Run this file directly to see the output.

```
uv run ./path/to/book.py
```
"""

from dataclasses import dataclass
from typing import Final


@dataclass
class Book:
    """Represents a book with basic bibliographic information.

    This data class is an example of a *product type* that groups multiple fields together using
    Python's `@dataclass` decorator.
    It supports structural equality, automatic `__repr__`, and field-based initialization.

    ## Usage:
    Use this class to store information about books, such as title, year, and author.
    Useful for educational examples or simple bibliographic models.

    ### Example 1: Basic initialization

    >>> book = Book("The Two Towers", 1954, "J.R.R. Tolkien")

    ### Example 2: Using default author

    >>> book = Book("Unknown Manuscript", 1900)

    :ivar title: The title of the book.
    :type title: str
    :ivar year: The year the book was published.
    :type year: int
    :ivar author: The author of the book. Defaults to "Unknown".
    :type author: str, optional
    """

    title: str
    year: int
    author: str = "Unknown"


# If run as a script, demonstrate dataclass capabilities.
if __name__ == "__main__":
    book: Final[Book] = Book(title="The Two Towers", year=1954, author="J.R.R. Tolkien")

    print("=== 📘 Representation: ===")
    # str() provides a human-readable format
    print(f"str(book): {str(book)}")
    # repr() is more technical and precise
    print(f"repr(book): {repr(book)}")

    print("\n=== 🔍 Field access ===")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.year}")

    print("\n=== 🧪 Equality comparison ===")
    same_book = Book("The Two Towers", 1954, "J.R.R. Tolkien")
    print(f"book == same_book? {book == same_book}")  # True if all fields match
