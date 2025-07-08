"""
user.py — Demonstrates property encapsulation and mutability with validation.

This module defines a `User` class that illustrates the use of the `@property` decorator to:
- encapsulate access to a private attribute (`__name`)
- validate updates to ensure the name is not empty
- reset the name to a default value when deleted

Intended for educational use to demonstrate property control patterns in Python.

## Usage

Run this file directly to see the behavior of the `User` class:

```bash
uv run ./path/to/user.py
```

Expected output:
```
Kurumi
Miki
Anonymous
Traceback (most recent call last):
  ...
ValueError: Name cannot be empty
```
"""


class User:
    """
    Represents a user with a mutable name property, including validation and deletion behavior.

    The name is stored privately and accessed via a property that enforces non-empty values.
    If the name is deleted, it resets to a default value ("Anonymous").
    """

    __name: str  # Private attribute to store the user's name

    def __init__(self, name: str):
        """
        Initializes a new user with the given name.

        :param name: The initial name of the user.
        :raises ValueError: If the name is empty or only whitespace.
        """
        self.__name = name

    @property
    def name(self) -> str:
        """
        Gets the user's name.

        :return: The current name of the user.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the user's name after validating it's not empty.

        :param value: The new name to assign.
        :raises ValueError: If the provided name is empty or whitespace.
        """
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    @name.deleter
    def name(self) -> None:
        """
        Deletes the user's name by resetting it to "Anonymous".
        """
        self.__name = "Anonymous"


if __name__ == "__main__":
    user = User("Kurumi")
    print(user.name)  # Kurumi

    user.name = "Miki"
    print(user.name)  # Miki

    del user.name
    print(user.name)  # Anonymous

    user.name = "  "  # Raises ValueError: Name cannot be empty
