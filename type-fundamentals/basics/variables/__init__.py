"""
variables — Demonstrates Python's treatment of mutable and immutable variables.

This package contains examples illustrating:
- How variable reassignment works in Python.
- The distinction between mutable and immutable objects.
- Conventions around constants and the use of `Final` for static type checking.
- Property decorators for computed properties in classes.
"""

from .author import Author
from .user import User

__all__ = ["Author", "User"]
