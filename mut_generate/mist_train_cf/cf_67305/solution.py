"""
QUESTION:
Write a function `longest_diagonal_prime` that takes a 4-dimensional array of integers and a prime number as input. The function should find the longest diagonal in the hypercube where the product of its elements equals the target prime number. A diagonal refers to a sequence starting from any element in the 4D array and moving in a fixed direction, changing all four coordinates at a time. If no such diagonal can be found, return a suitable message. The input cube can be of varying size and can contain both positive and negative integers.
"""

from math import prod

def longest_diagonal_prime(hypercube, prime):
    if not is_prime(prime):
        return "Input is not prime."

    max_length = min(len(hypercube), len(hypercube[0]), len(hypercube[0][0]), len(hypercube[0][0][0]))
    longest_diagonal = []

    for w in range(len(hypercube)):
        for z in range(len(hypercube[0])):
            for y in range(len(hypercube[0][0])):
                for x in range(len(hypercube[0][0][0])):
                    length = min(max_length, len(hypercube) - w, len(hypercube[0]) - z, len(hypercube[0][0]) - y, len(hypercube[0][0][0]) - x)
                    diagonal = [hypercube[w+i][z+i][y+i][x+i] for i in range(length)]
                    if prod(diagonal) == prime and len(diagonal) > len(longest_diagonal):
                        longest_diagonal = diagonal
    
    if len(longest_diagonal) == 0:
        return "No diagonal found."
    else:
        return longest_diagonal

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True