"""
connection.py — Demonstrates the use of an enum with pattern matching in Python.

This module defines a ConnectionState enum to represent the status of a connection and a function
`handle_connection` that uses structural pattern matching to return an appropriate message for each
state. It includes a fallback case to handle invalid inputs.

Primarily intended for educational purposes to illustrate how enums and match-case statements can be
used together in Python.

## Usage

Run this script directly to see how different connection states are handled.
```bash
uv run ./path/to/connection.py
```
"""

from enum import Enum, auto


class ConnectionState(Enum):
    """
    Represents the possible states of a network connection.

    :cvar CONNECTED: Indicates that the connection has been successfully established.
    :cvar DISCONNECTED: Indicates that the connection has been terminated or lost.
    :cvar IN_PROGRESS: Indicates that a connection attempt is currently underway.
    """

    CONNECTED = auto()
    DISCONNECTED = auto()
    IN_PROGRESS = auto()


def handle_connection(state: ConnectionState) -> str:
    """
    Returns a descriptive message based on the current connection state.

    Uses structural pattern matching to determine the appropriate response for each possible state
    of a connection.

    :param state: The current state of the connection.
    :type state: ConnectionState
    :return: A message describing the connection status.
    :rtype: str
    :raises ValueError: If the provided state does not match any known ConnectionState.
    """
    match state:
        case ConnectionState.CONNECTED:
            return "Connection established successfully."
        case ConnectionState.DISCONNECTED:
            return "Connection has been lost."
        case ConnectionState.IN_PROGRESS:
            return "Connection is currently being established."
        case _:  # Python does not enforce exhaustiveness checking
            raise ValueError(f"Invalid connection state: {state}")


if __name__ == "__main__":
    # Example usage of the ConnectionState enum and handle_connection function
    print(handle_connection(ConnectionState.CONNECTED))
    print(handle_connection(ConnectionState.DISCONNECTED))
    print(handle_connection(ConnectionState.IN_PROGRESS))
    # noinspection PyTypeChecker
    print(
        handle_connection("UNKNOWN")
    )  # This will not match any case demonstrating the fallback behavior
