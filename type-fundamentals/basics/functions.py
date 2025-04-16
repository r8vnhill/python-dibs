"""
Module: basics.functions

This module contains illustrative examples of how to define and invoke different types of functions in Python.
It demonstrates key language features such as positional and default arguments, variadic arguments (`*args`,
`**kwargs`), pattern matching, and runtime behavior of type hints.

## Functions included:
- `add`: Adds two integers.
- `multiply`: Multiplies two integers (demonstrates type hint vs runtime behavior).
- `summon`: Returns a formatted message summoning a character to a location.
- `throw_pokeballs`: Accepts a variable number of targets (names or numbers) and prints a response.
- `describe_technique`: Prints a named technique and any number of descriptive attributes.
- `cast_spell`: Simulates a spell being cast with optional companions and spell metadata.

This module is intended for educational and demonstrative purposes.
"""


def add(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    This function performs a basic arithmetic addition between the two input values.

    ## Examples:

    >>> add(2, 3)
    5

    >>> add(-7, 10)
    3

    :param a: The first number to add.
    :param b: The second number to add.
    :return: The result of adding `a` and `b`.
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    Returns the product of two integers.

    This function multiplies the two provided integers and returns the result.

    ## Examples:

    >>> multiply(4, 5)
    20

    >>> multiply(-3, 6)
    -18

    >>> multiply(0, 99)
    0

    :param a: The first number to multiply.
    :param b: The second number to multiply.
    :return: The result of multiplying `a` by `b`.
    """
    return a * b


def summon(character: str, location: str = "Rivendell") -> str:
    """
    Returns a message stating that a character has been summoned to a location.

    If no location is provided, the default is "Rivendell".

    ## Examples:

    >>> summon("Gandalf")
    'Gandalf has been summoned to Rivendell.'

    >>> summon("Aragorn", "Minas Tirith")
    'Aragorn has been summoned to Minas Tirith.'

    :param character: The name of the character being summoned.
    :param location: The location to which the character is summoned (default is "Rivendell").
    :return: A formatted string describing the summoning.
    """
    return f"{character} has been summoned to {location}."


def throw_pokeballs(*targets: str | int) -> None:
    """
    Prints a message for each target, simulating the action of throwing Pokéballs.

    This function accepts a variable number of arguments, where each argument can be a Pokémon name (`str`) or a Pokédex
    number (`int`).
    It prints a different message depending on the type of the target using structural pattern matching.

    ## Examples:

    >>> throw_pokeballs("Pikachu", 25, "Charmander")
    You threw a Pokéball at Pikachu!
    You threw a Pokéball at Pokémon #25!
    You threw a Pokéball at Charmander!

    :param targets: A variable number of Pokémon names or Pokédex numbers.
    :return: None
    """
    for target in targets:
        match target:
            case str():
                print(f"You threw a Pokéball at {target}!")
            case int():
                print(f"You threw a Pokéball at Pokémon #{target}!")


def describe_technique(name: str, **details) -> None:
    """
    Prints the name of a technique along with any additional descriptive details.

    This function accepts a technique name and any number of keyword arguments that describe attributes of the technique
    (e.g., speed, power, type).

    ## Examples:

    >>> describe_technique("Phantom Mirage", speed="extreme", class_type="offensive")
    Technique: Phantom Mirage
      speed: extreme
      class_type: offensive

    :param name: The name of the technique.
    :param details: Arbitrary keyword arguments describing the technique.
    :return: None
    """
    print(f"Technique: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")


def cast_spell(caster: str, *companions: str, **spell_details) -> None:
    """
    Simulates casting a spell by a caster, optionally assisted by companions, and defined by additional spell details.

    This function prints out a message indicating who is casting the spell, who is assisting (if any), and any
    spell-related attributes such as element, power, duration, etc., passed as keyword arguments.

    ## Examples:

    >>> cast_spell("Akko", "Lotte", "Sucy", element="light", power="unstable")
    Akko begins casting a spell!
    Assisted by: Lotte, Sucy
    Element: light
    Power: unstable

    >>> cast_spell("Merlin", element="fire", duration="5s")
    Merlin begins casting a spell!
    Element: fire
    Duration: 5s

    :param caster: The name of the spellcaster.
    :param companions: Optional list of characters assisting the caster.
    :param spell_details: Arbitrary keyword arguments describing the spell's attributes.
    :return: None
    """
    print(f"{caster} begins casting a spell!")
    if companions:
        print("Assisted by:", ", ".join(companions))
    for key, value in spell_details.items():
        print(f"{key.capitalize()}: {value}")


if __name__ == '__main__':
    print("▶️ add(2, 3)")
    print(add(2, 3))  # ➜ 5

    print("\n▶️ multiply('💥', 3)")
    # ❗ Although 'multiply' is annotated to return an int,
    # this call returns a string because Python does not enforce types at runtime.
    # noinspection PyTypeChecker
    print(multiply("💥", 3))  # ➜ 💥💥💥

    print("\n▶️ summon('Gandalf')")
    print(summon("Gandalf"))  # ➜ Gandalf has been summoned to Rivendell.

    print("\n▶️ summon('Aragorn', 'Minas Tirith')")
    print(summon("Aragorn", "Minas Tirith"))  # ➜ Aragorn has been summoned to Minas Tirith.

    print("\n▶️ throw_pokeballs('Pikachu', 25, 'Charmander')")
    throw_pokeballs("Pikachu", 25, "Charmander")
    # ➜ You threw a Pokéball at Pikachu!
    # ➜ You threw a Pokéball at Pokémon #25!
    # ➜ You threw a Pokéball at Charmander!

    print("\n▶️ describe_technique('Phantom Mirage', speed='extreme', class_type='offensive')")
    describe_technique("Phantom Mirage", speed="extreme", class_type="offensive")
    # ➜ Technique: Phantom Mirage
    # ➜   speed: extreme
    # ➜   class_type: offensive

    print("\n▶️ cast_spell('Akko', 'Lotte', 'Sucy', element='light', power='unstable')")
    cast_spell("Akko", "Lotte", "Sucy", element="light", power="unstable")
    # ➜ Akko begins casting a spell!
    # ➜ Assisted by: Lotte, Sucy
    # ➜ Element: light
    # ➜ Power: unstable
