"""
data_classes – Examples of Python product types using the `@dataclass` decorator.

This package contains minimal examples demonstrating:
- Differences between regular classes and data classes (`armor`)
- Basic usage of dataclasses to model records (`book`)
- Immutability with frozen dataclasses (`comic`)
- Conversion of dataclass instances to tuples (`videogame`)
- Computed properties and methods in dataclasses (`pokemon`)
- Simple validation in dataclasses (`song`)
- Safe object mutation using `replace` from `dataclasses` (`ghoul`)
"""

from .armor import Armor
from .book import Book
from .comic import Comic
from .videogame import VideoGame
from .pokemon import Pokemon
from .song import Song
from .ghoul import Ghoul

__all__ = ["Armor", "Book", "Comic", "VideoGame", "Pokemon", "Song", "Ghoul"]
