"""
enum module — Demonstrates sum types using Python enums.

This package contains minimal examples demonstrating:

- How to model sum types using Python’s `Enum` and `auto`
- How to define and use logging levels with structured output (`log.py`)
- How to perform pattern matching on enums for connection state handling (`connection.py`)

Each example is designed for clarity and pedagogical use in teaching algebraic data types.
"""

from .log import LogLevel, log
from .connection import ConnectionState, handle_connection

__all__ = [
    "LogLevel",
    "log",
    "ConnectionState",
    "handle_connection",
]
