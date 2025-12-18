"""
QUESTION:
Create a function named `contains_three_consecutive_digits` that takes an integer as input and returns a boolean indicating whether the integer contains a sequence of 3 or more identical consecutive digits. Use this function to calculate the sum of the modified harmonic series up to the 1200th term, excluding terms where the denominator contains a sequence of 3 or more identical consecutive digits, and round the result to 10 decimal places.
"""

def contains_three_consecutive_digits(n):
    n = str(n)
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] == n[i + 2]:
            return True
    return False