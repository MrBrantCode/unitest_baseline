"""
QUESTION:
Write a function `generate_sequence(n)` that takes an integer `n` as input and returns the nth number in the sequence where each number is formed by counting the number of consecutive occurrences of each digit in the previous number and concatenating the count followed by the digit itself. The function should satisfy the constraint 1 ≤ n ≤ 100.
"""

def generate_sequence(n):
    sequence = "1"
    
    for _ in range(n-1):
        next_number = ""
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i-1]:
                count += 1
            else:
                next_number += str(count) + sequence[i-1]
                count = 1
        next_number += str(count) + sequence[-1]
        sequence = next_number
    
    return sequence