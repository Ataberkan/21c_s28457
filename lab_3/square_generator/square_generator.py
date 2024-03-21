class SquareGenerator:
    def generate_squares(self, start, end):
        """Generates a list of squares from start to end, inclusive.

        Raises:
            ValueError: If end < start.
        """
        if end < start:
            raise ValueError("The end value cannot be less than the start value.")
        return [x ** 2 for x in range(start, end + 1)]


# Example usage with exception handling
try:
    generator = SquareGenerator()
    print(generator.generate_squares(10, 1))
except ValueError as e:
    print(e)

# Task 9 #
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("The end value cannot be less than the start value.")
        return [x**3 for x in range(start, end + 1)]