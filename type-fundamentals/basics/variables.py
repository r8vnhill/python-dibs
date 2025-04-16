"""
Module: basics.variables

Demonstrates the use of variables and constants in Python.

This example highlights the difference between regular variables (which are mutable) and constants declared with `Final`
from the `typing` module.
Although Python does not enforce immutability at runtime, tools like type checkers (e.g., mypy or Pyright) will warn
when a constant marked as `Final` is reassigned.

## Concepts Illustrated:

- Variable assignment and reassignment
- Use of `Final` to indicate intent for a constant
- Behavior of constants and how type checkers handle reassignment

This module is intended for educational purposes to explain basic variable semantics in Python.
"""
from typing import Final

if __name__ == '__main__':
    name = "Emilia"
    mana = 80
    print(f"Name: {name}, Mana: {mana}")

    # Regular variables can be reassigned freely
    mana = 100
    print(f"Updated Mana: {mana}")

    # Declaring a constant using Final (not enforced at runtime)
    MAX_MANA: Final[int] = 100
    print(f"Max Mana: {MAX_MANA}")

    # Reassigning a Final variable is technically allowed at runtime but will trigger warnings from static type
    # checkers
    MAX_MANA = 120  # ⚠️ Warning from type checkers (e.g., mypy, Pyright)
    print(f"Updated Max Mana: {MAX_MANA}")
