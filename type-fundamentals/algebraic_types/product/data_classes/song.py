"""
song.py — A simple example of using Python's dataclass with validation.

This module defines a `Song` data class that stores the title and release year of a song.
It includes basic post-initialization validation to ensure that the year is a positive integer.

## Features:
- Uses `@dataclass` for concise data modeling.
- Includes validation logic via `__post_init__` to enforce business rules.
- Provides a minimal usage example when run as a script.

## Usage:

```bash
uv run song.py
```

Attempting to create a song with a non-positive year will raise a `ValueError`.
"""

from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a musical track with a title and release year.

    This data class models a song using its title and the year it was released.
    It includes a post-initialization check to ensure that the year is a positive integer.

    :ivar title: The title of the song.
    :type title: str
    :ivar year: The release year of the song (must be a positive integer).
    :type year: int
    """

    title: str
    year: int

    def __post_init__(self):
        if self.year < 1:
            raise ValueError("Year must be a positive integer")


if __name__ == "__main__":
    # Valid song
    song = Song(title="Enemy to Injustice", year=2014)
    print(song)

    # Invalid song — raises ValueError
    invalid_song = Song(title="Invalid Song", year=0)
