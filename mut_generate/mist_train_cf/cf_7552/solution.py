"""
QUESTION:
Create a function `square_and_divisible` that takes a list of integers as input and returns a list containing the square of each element. For each square, if it is divisible by any prime number up to 31, append the string "divisible by a prime number" to the square. The output list should not contain any duplicates and must be generated without using built-in functions like set().
"""

def square_and_divisible(numbers):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # List of prime numbers up to 31
    unique_squares = []

    for num in numbers:
        square = num ** 2
        square_str = str(square)
        if any(square % prime == 0 for prime in primes):
            square_str += " divisible by a prime number"
        
        if square_str not in unique_squares:
            unique_squares.append(square_str)

    return unique_squares