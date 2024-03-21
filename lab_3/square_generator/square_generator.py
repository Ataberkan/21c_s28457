from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        """Generates a list of squares from start to end, inclusive.

        This method is abstract and must be implemented by subclasses.

        Raises:
            ValueError: If end < start.
        """
        pass


# Task 9 #
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        """Generates a list of cubes from start to end, inclusive.

        Overrides the abstract method in SquareGenerator to generate cubes.

        Raises:
            ValueError: If end < start.
        """
        if start >= end:
            raise ValueError("The end value cannot be less than the start value.")
        return [x ** 3 for x in range(start, end + 1)]


# Example usage with exception handling
try:
    generator = CubicGenerator()
    print(generator.generate_squares(1, 10))
except ValueError as e:
    print(e)
