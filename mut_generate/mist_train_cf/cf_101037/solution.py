"""
QUESTION:
Write a function `find_new_sequences(numbers)` that takes a list of integers as input and returns a list of all possible new sequences that satisfy the following rules:
- Each number in the new sequence must be a prime number.
- The new sequence must have exactly 4 numbers.
- Each number in the new sequence must be created by subtracting the digits of two different numbers in the given sequence. 
The function should return the first new sequence it finds.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def subtract_digits(a, b):
    return abs(sum(int(d) for d in str(a)) - sum(int(d) for d in str(b)))

def find_new_sequences(numbers):
    new_sequences = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = subtract_digits(numbers[i], numbers[j])
            if is_prime(diff) and diff not in new_sequences:
                new_sequences.append(diff)
                if len(new_sequences) == 4:
                    return new_sequences