"""
QUESTION:
Create a function named `assign_numerical_value` that takes a string as input. The function should map each letter of the string to a prime number where 'A' maps to 2, 'B' maps to 3, 'C' maps to 5, and so on, and return the product of these prime numbers. The input string may contain both uppercase and lowercase letters, but the function should be case-insensitive. The function should ignore any characters in the string that are not letters.
"""

def assign_numerical_value(string):
    prime_numbers = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13, 'G': 17, 'H': 19, 'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47, 'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71, 'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97, 'Z': 101}
    product = 1

    for letter in string.upper():
        if letter in prime_numbers:
            product *= prime_numbers[letter]

    return product