from collections import namedtuple


def get_coordinates() -> tuple[int, int]:
    """
    Returns a tuple of two integers representing coordinates.
    This function is a simple example of how to return multiple values using a tuple.
    The returned tuple can be unpacked into separate variables for easier access.

    ## Examples:
    >>> a, b = get_coordinates()
    >>> print(a, b)
    42 24

    :return: A tuple containing two integers.
    """
    return 42, 24


if __name__ == "__main__":
    print("\n▶️ position = (10, 5)")
    position = (10, 5)
    print(f"Position: {position}")

    print("\n▶️ x, u = get_coordinates()")
    x, y = get_coordinates()
    print(f"Coordinates: {x}, {y}")

    print("\n▶️ dimensions = (1920, 1080, 60)")
    dimensions = (1920, 1080, 60)
    print(f"Dimensions: {dimensions[0]}x{dimensions[1]}@{dimensions[2]}Hz")

    print("\n▶️ Resolution = namedtuple('Resolution', ['width', 'height', 'refresh'])")
    Resolution = namedtuple("Resolution", ["width", "height", "refresh"])
    screen = Resolution(1920, 1080, 60)

    print(f"{screen.width}x{screen.height}@{screen.refresh}Hz")
