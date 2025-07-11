"""
compiler.py — Enum iteration example

Demonstrates how to iterate over an enumeration in Python, accessing both the name and the value of
each enum member.
This is useful for scenarios such as displaying optimization phases with their descriptions.
"""

from enum import Enum


class OptimizationPass(Enum):
    """Represents different optimization passes in a compilation pipeline.

    Each member corresponds to a common optimization technique applied during the compilation or
    transformation of code.
    The associated value is a human-readable description of the pass.

    :cvar INLINE_FUNCTIONS: Replaces function calls with their bodies to reduce call overhead.
    :cvar REMOVE_DEAD_CODE: Removes code that is never executed.
    :cvar FOLD_CONSTANTS: Simplifies constant expressions at compile time.
    """

    INLINE_FUNCTIONS = "Inline functions to reduce call overhead."
    REMOVE_DEAD_CODE = "Remove code that is never executed."
    FOLD_CONSTANTS = "Replace expressions with constant values where possible."


def next_pass(current: OptimizationPass) -> OptimizationPass:
    """Returns the next optimization pass in declaration order.

    Cycles through the `OptimizationPass` enum values.
    If the current pass is the last in the list, wraps around to return the first.

    :param current: The current optimization pass.
    :return: The next optimization pass in the sequence.
    """
    passes = list(OptimizationPass)
    index = passes.index(current)
    return passes[(index + 1) % len(passes)]


if __name__ == "__main__":
    # Iterate over all enum members and print their name and description
    for phase in OptimizationPass:
        print(f"Optimization phase: {phase.name} ({phase.value})")

    # Create a list of formatted strings for each enum member and print it
    # This demonstrates a more compact way to access enum names and values
    print([f"{p.name} ({p.value})" for p in OptimizationPass])

    # Demonstrate cycling through optimization passes
    for phase in OptimizationPass:
        print(f"Next optimization pass after {phase.name}: {next_pass(phase).name}")
