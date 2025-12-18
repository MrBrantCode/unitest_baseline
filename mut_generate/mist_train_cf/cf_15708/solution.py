"""
QUESTION:
Create a function `calculate_hypotenuse(a, b)` that calculates the length of the hypotenuse of a right-angle triangle given the lengths of its two sides, represented by positive integers `a` and `b`. The function should handle inputs up to `10^9`, provide an error message and exit if the input is invalid (e.g., negative numbers, non-integer values), and not use any built-in functions or libraries for calculating the hypotenuse. The function should also implement its own square root function, handle cases where the hypotenuse is a very large number (e.g., greater than `10^9`), and return the length of the hypotenuse rounded to 2 decimal places. The time complexity of the function should be O(1) and the space complexity should be O(1).
"""

def calculate_hypotenuse(a, b):
    # Check if the inputs are valid
    if a <= 0 or b <= 0 or not isinstance(a, int) or not isinstance(b, int):
        print("Invalid input. Please enter positive integers for the lengths of the sides.")
        return

    # Calculate the square of the hypotenuse using the Pythagorean theorem
    c_squared = a ** 2 + b ** 2

    # Check if the hypotenuse is too large
    if c_squared > 10 ** 18:
        print("Error: Hypotenuse is too large to calculate.")
        return

    # Calculate the hypotenuse by finding the square root of the squared hypotenuse
    hypotenuse = square_root(c_squared)

    # Round the hypotenuse to 2 decimal places
    hypotenuse = round(hypotenuse, 2)

    return hypotenuse


def square_root(n):
    # Use the Babylonian method to find the square root of a number

    # Check if the number is negative
    if n < 0:
        print("Error: Cannot calculate square root of a negative number.")
        return

    # Set the initial guess for the square root
    guess = n / 2

    # Iterate until the guess is close enough to the actual square root
    while True:
        new_guess = (guess + n / guess) / 2
        if abs(new_guess - guess) < 0.00001:
            break
        guess = new_guess

    return new_guess