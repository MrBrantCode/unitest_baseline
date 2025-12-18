"""
QUESTION:
Write a function named `locate_seven_between_primes` that takes a string sequence as input. The function should check for the presence of the digit '7' in the sequence, excluding its occurrence at the start and end of the sequence, and verify that it is surrounded by prime numbers on both sides. The function should return the index position of the '7' digit in the cleaned sequence of numbers if found, and -1 otherwise. The function should ignore any non-digit characters in the input sequence.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def locate_seven_between_primes(sequence):
    cleaned_sequence = ''.join(filter(str.isdigit, sequence))
    for i in range(1, len(cleaned_sequence)-1):
        if cleaned_sequence[i] == "7":
            if is_prime(int(cleaned_sequence[i-1])) and is_prime(int(cleaned_sequence[i+1])):
                return i
    return -1