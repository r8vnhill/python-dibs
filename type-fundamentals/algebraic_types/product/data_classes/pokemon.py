"""
pokemon.py – Demonstrates basic use of dataclasses with computed properties and methods.

This module defines a simple `Pokemon` class using the `@dataclass` decorator.
Each Pokémon has a name, HP, attack, and defense.
It includes a computed property for total stats and a method that mimics a Pokémon speaking its
name.

## Usage

Run this script directly to see the output of the `total_stats` property and `speak()` method.

```bash
uv run ./path/to/pokemon.py
```
"""

from dataclasses import dataclass


@dataclass
class Pokemon:
    """
    Represents a basic Pokémon with stats and a speaking behavior.

    This data class holds the core attributes of a Pokémon and provides a computed property to
    calculate total stats, as well as a method that simulates the Pokémon calling out its name.

    ## Usage:

    >>> espurr = Pokemon("Espurr", hp=234, attack=90, defense=101)
    >>> print(espurr.total_stats)
    >>> print(espurr.speak())

    :ivar name: The Pokémon's name.
    :ivar hp: Hit points representing the Pokémon's health.
    :ivar attack: The attack stat.
    :ivar defense: The defense stat.
    """

    name: str
    hp: int
    attack: int
    defense: int

    @property
    def total_stats(self) -> int:
        """
        Computes the total stats by summing hp, attack, and defense.

        :return: The total of the three stats.
        :rtype: int
        """
        return self.hp + self.attack + self.defense

    def speak(self) -> str:
        """
        Simulates the Pokémon speaking its name.

        :return: A string with the Pokémon's name followed by an exclamation mark.
        :rtype: str
        """
        return f"{self.name}!"


if __name__ == "__main__":
    # Create an instance of the Pokemon class
    snorunt = Pokemon(name="Snorunt", hp=210, attack=94, defense=94)

    # Print the sum of hp, attack, and defense using the computed property
    print("Total stats:", snorunt.total_stats)

    # Print the result of the Pokemon's speak() method
    print(snorunt.speak())
