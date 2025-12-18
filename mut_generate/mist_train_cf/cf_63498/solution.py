"""
QUESTION:
Implement a function `collatz(n, input_number)` that generates the Collatz sequence starting from `n` and calculates the position of `input_number` in the sequence, the corresponding sequence number, and the total number of steps to reach 1. The function should return a dictionary with these three pieces of information. The input `n` should be a positive integer, and the function should handle cases where `n` is less than 1.
"""

def collatz(n, input_number):
    if n < 1:
        return None

    sequence = [n]
    steps = 0
    position = None
    corr_seq_number = None

    while n != 1:
        if n == input_number:
            position = len(sequence) - 1
            corr_seq_number = n

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        sequence.append(n)
        steps += 1

    if n == input_number:
        position = len(sequence) - 1
        corr_seq_number = n

    return {"position": position, "sequence_number": corr_seq_number, "steps": steps}