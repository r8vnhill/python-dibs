"""
validator.py — Enum methods for validation strategies

Demonstrates how to define behavior (methods) on enum members using Python's `Enum` class.
Each enum member represents a different platform-specific strategy for validating usernames.

The `validate(name: str)` method is implemented directly in the enum and specialized per variant
using pattern matching (`match case`).

## Usage:
Run the script to validate a sample username against all defined strategies:

```bash
uv run path/to/validator.py
```
This will print whether the username is valid for each platform.
"""

from enum import Enum, auto


from enum import Enum, auto


class ValidationStrategy(Enum):
    """Represents different platform-specific strategies for validating usernames.

    Each enum member defines its own validation rules, which are encapsulated in the `validate()`
    method.

    :cvar WEB: Usernames must be 4–12 characters long and alphanumeric.
    :cvar MOBILE: Usernames must start with a letter, followed by letters, digits, or underscores.
    :cvar CONSOLE: Usernames must be exactly 8 characters long and contain no vowels.
    """

    WEB = auto()
    MOBILE = auto()
    CONSOLE = auto()

    def validate(self, name: str) -> bool:
        """Validates the given name according to the selected strategy.

        - `WEB`: Requires alphanumeric characters only, with a length between 4 and 12.
        - `MOBILE`: Requires the first character to be a letter. The rest can be alphanumeric or
          underscores.
        - `CONSOLE`: Requires exactly 8 characters and disallows vowels.

        :param name: The username string to validate.
        :return: `True` if the name satisfies the strategy’s rules, `False` otherwise.
        :raises ValueError: If the strategy is unrecognized (should not happen).
        """
        match self:
            case ValidationStrategy.WEB:
                return name.isalnum() and 4 <= len(name) <= 12
            case ValidationStrategy.MOBILE:
                return name[0].isalpha() and all(c.isalnum() or c == "_" for c in name)
            case ValidationStrategy.CONSOLE:
                return len(name) == 8 and not any(c in "aeiouAEIOU" for c in name)
            case _:
                raise ValueError(f"Unknown validation strategy: {self}")


if __name__ == "__main__":
    user = "Admin_01"

    for strategy in ValidationStrategy:
        print(f"{strategy.name}: {strategy.value}")
        print("✓ Valid" if strategy.validate(user) else "✗ Invalid")
        print()
