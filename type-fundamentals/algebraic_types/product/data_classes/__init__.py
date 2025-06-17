"""
data_classes – Examples of Python product types using the `@dataclass` decorator.

This package contains minimal examples demonstrating:
- Differences between regular classes and data classes (`armor`)
- Basic usage of dataclasses to model records (`book`)
"""

from .armor import Armor
from .book import Book

__all__ = ["Armor", "Book"]
