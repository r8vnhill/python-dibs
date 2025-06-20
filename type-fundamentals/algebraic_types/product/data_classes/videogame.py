"""
videogame.py – Demonstrates use of Python dataclasses and `astuple`.

This module defines a simple data class to represent a video game and shows how to convert an
instance into a tuple using `dataclasses.astuple`.

## Usage

Run this file directly to see a sample tuple unpacking of a video game instance.

```bash
uv run ./path/to/videogame.py
```
"""

from dataclasses import dataclass, astuple


@dataclass
class VideoGame:
    """
    Represents a video game with basic metadata.

    This class uses the `@dataclass` decorator to automatically generate useful methods such as
    `__init__`, `__repr__`, and `__eq__`.

    :ivar title: The title of the video game.
    :ivar developer: The company or studio that developed the game.
    """

    title: str
    developer: str


if __name__ == "__main__":
    # Create a VideoGame instance and convert it to a tuple of its fields
    title, developer = astuple(
        VideoGame(
            title="The Awesome Adventures of Captain Spirit",
            developer="Dontnod Entertainment",
        )
    )

    # Print each field separately after unpacking
    print(f"Title: {title}, Developer: {developer}")
