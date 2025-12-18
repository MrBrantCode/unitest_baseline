"""
QUESTION:
Write a function named `sum_multiples_of_4_and_7` that calculates the sum of the multiples of both 4 and 7 up to the largest perfect square less than or equal to a given number. The function should take one parameter `num`, which is the given number.
"""

def sum_multiples_of_4_and_7(num):
    # Find the largest perfect square less than or equal to the given number
    largest_square = int(num ** 0.5) ** 2

    # Initialize the sum of multiples
    sum_multiples = 0

    # Iterate from 4 to the largest square, incrementing by 4
    for i in range(4, largest_square + 1, 4):
        # Check if the current number is divisible by both 4 and 7
        if i % 7 == 0:
            sum_multiples += i

    return sum_multiples