from typing import Final


class Point:
    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @classmethod
    def from_tuple(cls, coords: (int, int)) -> "Point":
        return cls(coords[0], coords[1])

    @staticmethod
    def from_position(pos: "Position") -> "Point":
        return Point(pos.x, pos.y)

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y


class Position:
    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def move(self, dx: int, dy: int) -> "Position":
        return Position(self.__x + dx, self.__y + dy)

    @property
    def is_origin(self) -> bool:
        return self.__x == 0 and self.__y == 0

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y


class DenseLayer:
    __input_dim: int
    __output_dim: int
    __activation: str
    __use_bias: bool

    def __init__(self, *args: int, **kwargs: int | str | bool):
        if args:
            self.__input_dim = args[0]
            self.__output_dim = args[1]
        else:
            self.__input_dim = kwargs.get("input_dim", 0)
            self.__output_dim = kwargs.get("output_dim", 0)

        self.__activation = kwargs.get("activation", "relu")
        self.__use_bias = kwargs.get("use_bias", True)

    def summary(self) -> dict[str, int | str | bool]:
        return {
            "input_dim": self.__input_dim,
            "output_dim": self.__output_dim,
            "activation": self.__activation,
            "use_bias": self.__use_bias,
        }


if __name__ == "__main__":
    # region REGION NAME
    point: Final[Point] = Point(49, 41)
    print(point.x)  # 49
    print(point.y)  # 41
    # endregion REGION NAME

    # region REGION NAME
    position: Final[Position] = Position(86, 29)
    print(position.is_origin)  # False
    print(position.move(-86, -29).is_origin)  # True
    # endregion REGION NAME

    # region REGION NAME
    point_from_tuple: Final[Point] = Point.from_tuple((49, 41))
    print(point_from_tuple.x)
    # endregion REGION NAME

    # region REGION NAME
    point_from_position: Final[Point] = Point.from_position(position)
    print(point_from_position.x)
    # endregion REGION NAME

    # region REGION NAME
    # Using positional parameters
    layer1: Final[DenseLayer] = DenseLayer(128, 64)

    # Using named parameters
    layer2: Final[DenseLayer] = DenseLayer(
        input_dim=256, output_dim=128, activation="tanh", use_bias=False
    )

    # Using dynamically loaded configuration
    config = {"input_dim": 512, "output_dim": 256, "activation": "sigmoid"}
    layer3 = DenseLayer(**config)

    print(layer1.summary())
    print(layer2.summary())
    print(layer3.summary())
    # endregion REGION NAME
