"""
QUESTION:
Create a function named `five_mult_div_seq` that takes four parameters: `n`, `start_range`, `end_range`, and `m`, all of which are integers. The function should return the total count of the digit 5 in two sequences: an ascending sequence of numbers from `start_range` to `n-1` and a descending sequence of numbers from `end_range` to `n` (exclusive), both of which consist of numbers divisible by 9, 14, or `m`.
"""

def five_mult_div_seq(n: int, start_range: int, end_range: int, m: int) -> int:
    # Ascending sequence.
    ascending_sequence = [num for num in range(start_range, n) if num % 9 == 0 or num % 14 == 0 or num % m == 0]
    # Descending sequence.
    descending_sequence = [num for num in range(end_range, n, -1) if num % 9 == 0 or num % 14 == 0 or num % m == 0]
    
    # Combine both sequences.
    total_sequence = ascending_sequence + descending_sequence

    count = sum([str(num).count('5') for num in total_sequence])
    return count