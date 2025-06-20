"""
ghoul.py – Demonstrates the use of immutable dataclasses and safe object mutation using `replace`.

This module defines an immutable `Ghoul` class using Python's `@dataclass(frozen=True)` decorator.
It also shows how to simulate changes (such as reducing hunger) by creating a new instance
instead of mutating the original, preserving immutability.

## Usage

Run the script directly to simulate a ghoul consuming food and reducing its hunger.

```bash
uv run ./path/to/ghoul.py
```
"""

from dataclasses import dataclass, replace
from typing import Final


@dataclass(frozen=True)
class Ghoul:
    """
    Represents a ghoul with a name and hunger level.

    This dataclass is marked as frozen, meaning instances are immutable after creation.
    Use `dataclasses.replace` to create a modified copy with updated values.

    :ivar name: The name of the ghoul.
    :type name: str
    :ivar hunger: The current hunger level (higher means hungrier).
    :type hunger: int
    """

    name: str
    hunger: int


if __name__ == "__main__":
    # Initial state: Ghoul is hungry
    nishio_before: Final[Ghoul] = Ghoul(name="Nishiki Nishio", hunger=77)
    print(nishio_before)

    print("Eating...")

    # Create a new Ghoul instance with reduced hunger
    nishio_after: Final[Ghoul] = replace(
        nishio_before, hunger=nishio_before.hunger - 10
    )
    print(nishio_after)
