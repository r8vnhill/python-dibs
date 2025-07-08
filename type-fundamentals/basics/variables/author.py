"""
author.py — Demonstrates encapsulation and immutability using private fields and read-only
properties.

This module defines a simple `Author` class that encapsulates an author's name and a list of works.
The works are exposed through a read-only property as an immutable tuple to prevent accidental
modification.

## Usage

Run this script directly to see how the `Author` class behaves with read-only access to its works.

```bash
uv run ./path/to/author.py
```
"""


class Author:
    """
    Represents an author and their literary works.

    This class encapsulates an author's name and their list of works.
    The list of works is exposed as a read-only property to ensure immutability from the outside.

    Attributes are kept private to promote encapsulation.
    """

    __name: str
    __works: list[str]

    def __init__(self, name: str, works: list[str]):
        """
        Initializes a new Author instance.

        :param name: The author's name.
        :type name: str
        :param works: A list of the author's published works.
        :type works: list[str]
        """
        self.__name = name
        self.__works = works

    @property
    def works(self) -> tuple[str, ...]:
        """
        Returns the author's works as an immutable tuple.

        This prevents external code from modifying the internal list, preserving encapsulation and
        immutability.

        :return: A tuple containing the author's works.
        :rtype: tuple[str, ...]
        """
        return tuple(self.__works)


if __name__ == "__main__":
    author = Author(name="Junji Ito", works=["Uzumaki", "Tomie", "Gyo"])
    print(f"Works: {author.works}")

    # This line will raise an AttributeError because 'works' is a read-only property
    # author.works = ["At the mountains of madness"]

    # This will raise an AttributeError because tuples are immutable
    # author.works.append("Souichi's Diary of Curses")
