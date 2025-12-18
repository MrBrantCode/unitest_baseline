"""
QUESTION:
Set

Given the sequence a_1, a_2, .., a_N.

How many values ​​are there in this sequence?

input


N
a_1 a_2 ... a_N


output

Output the number of types of values ​​in the sequence.

Constraint

* 1 \ leq N \ leq 10 ^ 5
* 1 \ leq a_i \ leq 10 ^ 9



Input example


6
8 6 9 1 2 1


Output example


Five






Example

Input

6
8 6 9 1 2 1


Output

5
"""

def count_unique_values(sequence):
    """
    Counts the number of unique values in the given sequence.

    Parameters:
    sequence (list of int): A list of integers representing the sequence.

    Returns:
    int: The number of unique values in the sequence.
    """
    return len(set(sequence))