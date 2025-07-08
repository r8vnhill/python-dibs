"""
mutability.py — Demonstrates Python's treatment of mutable and immutable variables.

This script showcases:
- How variable reassignment works in Python.
- The distinction between mutable and immutable objects.
- Conventions around constants and the use of `Final` for static type checking.
"""

from typing import Final

if __name__ == "__main__":
    # Basic variable declarations
    name = "Emilia"
    mana = 80
    print(f"Name: {name}, Mana: {mana}")

    # Variables in Python are dynamically typed and fully mutable by default
    mana = 100  # Reassignment is allowed
    print(f"Updated Mana: {mana}")

    # Demonstrating mutability with lists
    # `numbers` is a mutable list; elements can be modified or appended
    numbers = [1, 2, 3]
    numbers.append(4)  # Valid operation
    print(f"Updated Numbers: {numbers}")

    # Demonstrating immutability with strings
    # Strings in Python are immutable; this line would raise a TypeError at runtime
    # name[0] = "A"

    # Constants are usually written in ALL_CAPS, but Python doesn't enforce immutability
    MAX_MANA = 100
    print(f"Max Mana: {MAX_MANA}")
    MAX_MANA = 120  # Legal but discouraged — violates constant convention
    print(f"Updated Max Mana: {MAX_MANA}")

    # Use Final for type-checker-enforced constants (e.g., with mypy)
    SPIRIT_NAME: Final[str] = "Puck"
    print(f"Spirit Name: {SPIRIT_NAME}")
    SPIRIT_NAME = (
        "Muspel"  # ⚠️ mypy will flag this as an error, but Python will still run it
    )
    print(f"Updated Spirit Name: {SPIRIT_NAME}")
