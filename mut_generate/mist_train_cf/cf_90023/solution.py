"""
QUESTION:
Write a function `generate_sequence` that takes an integer `n` as input, where 1 ≤ n ≤ 100, and returns the nth number in the sequence. The sequence is generated based on the previous number, where each digit is counted consecutively and the count followed by the digit is concatenated to form the next number.
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