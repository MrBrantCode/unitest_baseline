"""
QUESTION:
Create a function named `number_type_analysis` that takes a list of positive whole numbers as input. The function should categorize the numbers into three lists: prime numbers, perfect squares, and perfect cubes, and calculate the rate of change (i.e., the proportion) of perfect squares and perfect cubes in the list. The function should be efficient and able to handle very large numbers. Note that a simple trial division method may not be sufficient for large prime numbers and more advanced algorithms may be needed.
"""

def number_type_analysis(numbers):
    primes = []
    perfect_squares = []
    perfect_cubes = []

    for num in numbers:
        # Check if the number is a perfect square
        if int(num ** 0.5) ** 2 == num:
            perfect_squares.append(num)

        # Check if the number is a perfect cube
        if round(num ** (1. / 3)) ** 3 == num:
            perfect_cubes.append(num)

        # Check if the number is prime
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    # Get the rates of change of perfect squares and perfect cubes
    perfect_squares_change = len(perfect_squares) / len(numbers)
    perfect_cubes_change = len(perfect_cubes) / len(numbers)

    return primes, perfect_squares, perfect_cubes, perfect_squares_change, perfect_cubes_change