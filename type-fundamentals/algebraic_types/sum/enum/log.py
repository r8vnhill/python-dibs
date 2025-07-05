"""
log.py — A simple logging utility using an enum for log levels.

Provides a lightweight logging mechanism with three severity levels: INFO, WARNING, and ERROR.
Uses the built-in `enum` module to define log levels and directs error messages to standard error
(`sys.stderr`) while other messages go to standard output.

## Usage:

Run this script directly to see example log messages.

```bash
uv run ./path/to/log.py
```
"""

import sys

from enum import Enum, auto


class LogLevel(Enum):
    """
    Represents the severity level of a log message.

    Defines three levels of logging:
    - INFO: General information or successful operations.
    - WARNING: Something unexpected or potentially problematic.
    - ERROR: A serious issue that requires attention.

    Used to categorize log messages and control their output behavior.
    """

    INFO = auto()
    WARNING = auto()
    ERROR = auto()


def log(level: LogLevel, message: str) -> None:
    """
    Logs a message with a specified severity level.

    Outputs the message to standard output for INFO and WARNING levels, and to standard error for
    ERROR level messages.

    :param level: The severity level of the log message.
    :type level: LogLevel
    :param message: The content of the log message.
    :type message: str
    """
    if level is LogLevel.ERROR:
        print(f"[{level.name}] {message}", file=sys.stderr)
    else:
        print(f"[{level.name}] {message}")


if __name__ == "__main__":
    log(LogLevel.INFO, "Thank you Mario!")
    log(LogLevel.ERROR, "But our princess is in another castle!")
