"""
QUESTION:
Write a function `print_permutations(numbers)` that prints all possible permutations of a list of numbers, where the list must have an even length, contain at least two odd numbers and two even numbers, and the permutations must satisfy the following conditions: 

- Each permutation must contain at least one even number.
- The even number should be at an odd index position in the permutation.
- The odd numbers should be in increasing order.
- The even numbers should be in decreasing order.
"""

import itertools

def print_permutations(numbers):
    # Check if the list satisfies the length requirement
    if len(numbers) % 2 != 0:
        print("Invalid list length. Length should be even.")
        return

    # Check if the list contains at least two odd numbers and two even numbers
    odd_count = 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count < 2 or even_count < 2:
        print("Invalid list content. List should contain at least two odd numbers and two even numbers.")
        return

    # Generate all permutations of the list
    all_permutations = itertools.permutations(numbers)

    # Filter permutations based on the given restrictions
    valid_permutations = []
    for permutation in all_permutations:
        # Check if the permutation contains at least one even number
        if any(num % 2 == 0 for num in permutation):
            # Check if the even number is at an odd index position
            if any(permutation[i] % 2 == 0 and i % 2 != 0 for i in range(len(permutation))):
                valid_permutations.append(permutation)

    # Print the valid permutations
    for permutation in valid_permutations:
        print(permutation)