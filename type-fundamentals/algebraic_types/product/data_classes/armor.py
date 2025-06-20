"""
armor.py - Demonstrates the difference between regular Python classes and data classes.

This script defines two armor types:
- `_Armor`: A manually implemented class with private fields.
- `Armor`: A data class with automatic support for structural equality and readable representation.

The goal is to illustrate key differences between:
- Identity (`is`) and structural equality (`==`)
- Manual class definitions vs. using the `@dataclass` decorator

## Usage

Run this script directly to see comparison results in the console.

```bash
uv run ./path/to/armor.py
```
"""

from dataclasses import dataclass


class _Armor:  # Preceding underscore just to distinguish it from the `Armor` data class
    """
    A manually implemented class representing an armored suit.

    This class uses private attributes and does not override comparison or representation methods.
    As a result, equality checks compare object identity (i.e., memory address) rather than field
    values.

    Intended for contrast with the `Armor` data class.
    """

    __model: str
    __power: int

    def __init__(self, model: str, power: int):
        """
        Initializes a new instance of the `_Armor` class.

        This constructor stores the model name and power level of the armor, both as private fields.

        :param model: The name or version of the armor (e.g., "Mark I").
        :type model: str
        :param power: The power level of the armor.
        :type power: int
        """
        self.__model = model
        self.__power = power


@dataclass
class Armor:
    """
    A lightweight data structure representing an armor model.

    This class is implemented as a dataclass, which provides automatic support for comparison and
    readable representations.
    Unlike manually defined classes, `dataclass` instances are compared based on their field values.

    ## Usage:
    You can create and compare instances of `Armor` easily:

    >>> a1 = Armor("Mark II", 100)
    >>> a2 = Armor("Mark II", 100)
    >>> print(a1 == a2)  # True

    The string representation is also user-friendly:

    >>> print(a1)  # Armor(model='Mark II', power=100)

    :ivar model: The name or version of the armor (e.g., "Mark II").
    :type model: str
    :ivar power: The armor's power level.
    :type power: int
    """

    model: str
    power: int


if __name__ == "__main__":
    print("=== 🔗 Reference comparison with regular class ===")
    mark1 = _Armor("Mark I", 75)
    mark1_clone = _Armor("Mark I", 75)
    print(f"mark1 == mark1_clone? {mark1 == mark1_clone}")  # False

    print("\n=== 📦 Content comparison with dataclass ===")
    mark2 = Armor("Mark II", 100)
    mark2_clone = Armor("Mark II", 100)
    print(f"mark2 == mark2_clone? {mark2 == mark2_clone}")  # True

    print("\n=== 🧠 Identity vs equality ===")
    a = Armor("Hulkbuster", 150)
    b = a
    c = Armor("Hulkbuster", 150)

    print(f"a == c? {a == c}")  # True – same content
    print(f"a is c? {a is c}")  # False – different objects
    print(f"a is b? {a is b}")  # True – same reference
