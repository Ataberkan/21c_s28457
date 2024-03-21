import math

# Task 1 #
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 2 #
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

print(generate_squares(1, 10))

# Task 3 #
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("The end value cannot be less than the start value.")
        return [x**2 for x in range(start, end + 1)]

# Example usage
generator = SquareGenerator()
print(generator.generate_squares(1, 10))

# Task 4 #
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("The end value cannot be less than the start value.")
        return [x ** 2 for x in range(start, end + 1)]

    def calculate_square_roots(self, numbers_list):
        return [math.sqrt(number) for number in numbers_list]


# Example usage
generator = SquareGenerator()
squares = generator.generate_squares(1, 10)
square_roots = generator.calculate_square_roots(squares)
print("Squares:", squares)
print("Square Roots:", square_roots)

# Task 5 #
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

