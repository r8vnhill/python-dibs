"""
Module: basics.cycles

Provides basic utilities for working with collections and control flow patterns such as loops and
conditional filtering.
This module includes example functions for printing, transforming, and filtering data, as well as
basic configuration loading logic.

The content is designed to demonstrate idiomatic Python with common language features like
comprehensions, iteration, and optional values.

## Included utilities:
- `print_characters`: Prints each character in a list.
- `double_numbers`: Doubles all numbers in a list.
- `filter_pairs`: Filters and returns only even numbers.
- `unique_elements`: Extracts unique (non-None) values from any iterable.
- `known_clan_members`: Converts a list of name/clan pairs into a filtered dictionary.
- `try_load_config`: Simulates loading configuration files.
- `load_first_valid_config`: Attempts to load configuration from multiple sources.

This module is intended for educational or foundational purposes.
"""

from typing import TypeVar, Iterable

T = TypeVar("T")


def print_characters(characters: list[str]) -> None:
    """
    Prints each character from the given list on a separate line.

    This function iterates over a list of strings (e.g., character names) and prints each one
    individually.

    Args:
        characters (list[str]): A list of strings to print.
    """
    for char in characters:
        print(char)


def double_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list with all input numbers multiplied by 2.

    This function applies a transformation to each element in the list using a list comprehension,
    producing a list where each number is doubled.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: A new list with each number doubled.
    """
    return [x * 2 for x in numbers]


def filter_pairs(numbers: list[int]) -> list[int]:
    """
    Filters and returns only the even numbers from the input list.

    This function uses a list comprehension to select elements that are divisible by 2.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: A new list containing only the even numbers from the original list.
    """
    return [x for x in numbers if x % 2 == 0]


def unique_elements(elements: Iterable[T]) -> set[T]:
    """
    Returns a set of unique, non-None elements from the given iterable.

    This function eliminates duplicates and filters out `None` values, making it useful for cleaning
    up collections before further processing.

    Args:
        elements (Iterable[T]): An iterable of elements, possibly containing duplicates or `None`.

    Returns:
        set[T]: A set of unique elements excluding any `None` values.
    """
    return {x for x in elements if x is not None}


def known_clan_members(data: list[tuple[str, str | None]]) -> dict[str, str]:
    """
    Extracts known clan affiliations from a list of character–clan pairs.

    This function filters out entries where the clan is `None`, and constructs a dictionary mapping
    character names to their known clan names.

    Args:
        data (list[tuple[str, str | None]]): A list of (character, clan) pairs, where clan may be
            `None`.

    Returns:
        dict[str, str]: A dictionary of character names with known (non-None) clan affiliations.
    """
    return {
        char_name: char_clan for char_name, char_clan in data if char_clan is not None
    }


def try_load_config(source: str) -> int | None:
    """
    Simulates loading a configuration from the given source path.

    This function pretends to load a configuration file and returns a fixed configuration ID if the
    source is `"default.yaml"`.
    For all other values, it logs an error and returns `None`.

    Args:
        source (str): The name or path of the configuration source.

    Returns:
        int | None: A fixed configuration ID (420) if the source is valid, otherwise `None`.
    """
    print(f"🔍 Trying to load configuration from '{source}'")
    if source == "default.yaml":
        print("✅ Configuration loaded successfully.")
        return 420
    else:
        print("❌ Invalid configuration.")
        return None


def load_first_valid_config(sources: list[str]) -> int | None:
    """
    Attempts to load the first valid configuration from a list of sources.

    This function iterates through a list of configuration sources and calls `try_load_config` on
    each one in order.
    It returns the first non-None result, stopping the search once a valid configuration is found.

    Args:
        sources (list[str]): A list of configuration source names or paths.

    Returns:
        int | None: The first valid configuration ID found, or `None` if none succeed.
    """
    index = 0
    while index < len(sources):
        config = try_load_config(sources[index])
        index += 1
        if config is not None:
            return config
    return None


if __name__ == "__main__":
    print("=== 🔁 print_characters ===")
    print_characters(["Rick", "Michonne", "Carl", "Negan", "Andrea"])
    print()

    print("=== 📦 double_numbers ===")
    print(double_numbers([1, 2, 3, 4, 5]))
    print()

    print("=== 🧮 filter_pairs ===")
    print(filter_pairs([1, 2, 3, 4, 5, 6]))
    print()

    print("=== 🧼 unique_elements ===")
    digimon_levels = ["Rookie", "Champion", "Rookie", "Ultimate", None, "Mega"]
    print(unique_elements(digimon_levels))
    print()

    print("=== 🗺️ known_clan_members ===")
    clan_members = [
        ("Chun-Woo Han", "Black Heaven and Earth"),
        ("Jin-Ie", None),
        ("So-Chun Hyuk", "Muran"),
        ("Sera Kang", "Muran"),
        ("Goomoonryong", None),
    ]
    clans = known_clan_members(clan_members)
    for name, clan in clans.items():
        print(f"{name} → {clan}")
    print()

    print("=== ⚙️ load_first_valid_config ===")
    config_sources = ["user.yaml", "project.yaml", "default.yaml"]
    result = load_first_valid_config(config_sources)
    if result is not None:
        print(f"🛠️ Loaded config ID: {result}")
    else:
        print("💥 No valid configuration found.")
