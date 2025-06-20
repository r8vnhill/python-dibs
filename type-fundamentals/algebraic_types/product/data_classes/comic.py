"""
comic.py – Immutable data model for comic books.

This module defines an immutable `Comic` data class using Python's `@dataclass(frozen=True)`
decorator.
Instances of this class cannot be modified after creation, making it suitable for representing fixed
records such as published comic book entries.

## Usage

Run the file to see how immutability works in practice.

```bash
uv run ./path/to/comic.py
```

Attempting to modify a field after creation will raise a `FrozenInstanceError`.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Comic:
    """
    Represents a comic book with a title and publisher.

    This data class is declared `frozen`, meaning its fields are immutable.

    :ivar title: The name of the comic (e.g., "Black Panther").
    :ivar publisher: The company that published the comic (e.g., "Marvel").
    """

    title: str
    publisher: str


if __name__ == "__main__":
    # Create an instance of the Comic data class
    comic = Comic(title="Batman: I Am Gotham", publisher="DC")

    # ❌ Attempting to modify an attribute of a frozen dataclass
    # This will raise a dataclasses.FrozenInstanceError because 'Comic' is immutable
    comic.publisher = "Marvel"
