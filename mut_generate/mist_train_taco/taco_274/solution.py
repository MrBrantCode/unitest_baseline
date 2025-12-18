"""
QUESTION:
Write a program which reads a sequence of $n$ integers $a_i (i = 1, 2, ... n)$, and prints the minimum value, maximum value and sum of the sequence.

Constraints

* $0 < n \leq 10000$
* $-1000000 \leq a_i \leq 1000000$

Input

In the first line, an integer $n$ is given. In the next line, $n$ integers $a_i$ are given in a line.

Output

Print the minimum value, maximum value and sum in a line. Put a single space between the values.

Example

Input

5
10 1 5 4 17


Output

1 17 37
"""

def analyze_sequence(sequence: list[int]) -> tuple[int, int, int]:
    """
    Analyzes a sequence of integers and returns the minimum value, maximum value, and sum.

    Parameters:
    sequence (list[int]): A list of integers to be analyzed.

    Returns:
    tuple[int, int, int]: A tuple containing the minimum value, maximum value, and sum of the sequence.
    """
    if not sequence:
        raise ValueError("The sequence must not be empty.")
    
    min_value = min(sequence)
    max_value = max(sequence)
    total_sum = sum(sequence)
    
    return min_value, max_value, total_sum