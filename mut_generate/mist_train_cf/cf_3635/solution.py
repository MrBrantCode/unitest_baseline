"""
QUESTION:
Write a function `print_permutations` that takes a list of numbers as input and prints out all possible permutations of the list, subject to the following conditions: 
- the length of the list must be even;
- the list must contain at least two odd numbers and two even numbers;
- each permutation must contain at least one even number at an odd index position;
- the odd numbers in the list are in increasing order;
- the even numbers in the list are in decreasing order.
"""

import itertools

def entance(numbers):
    # Check if the list satisfies the length requirement
    if len(numbers) % 2 != 0:
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
                # Check if the odd numbers are in increasing order
                odd_nums = [num for num in permutation if num % 2 != 0]
                if odd_nums == sorted(odd_nums):
                    # Check if the even numbers are in decreasing order
                    even_nums = [num for num in permutation if num % 2 == 0]
                    if even_nums == sorted(even_nums, reverse=True):
                        valid_permutations.append(permutation)

    # Print the valid permutations
    for permutation in valid_permutations:
        print(permutation)