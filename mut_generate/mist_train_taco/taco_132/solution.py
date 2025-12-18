"""
QUESTION:
Min Element

Given the sequence a_1, a_2, .., a_N.

Find the minimum number in this sequence.

If the minimum value is in more than one place, answer the one with the lowest number.

input


N
a_1 a_2 ... a_N


output

Output the smallest i such that a_i is the minimum value in the sequence.

Constraint

* 1 \ leq N \ leq 10 ^ 5
* 1 \ leq a_i \ leq 10 ^ 9



Input example


6
8 6 9 1 2 1


Output example


Four






Example

Input

6
8 6 9 1 2 1


Output

4
"""

def find_min_element_index(sequence):
    """
    Finds the 1-based index of the first occurrence of the minimum value in the given sequence.

    Parameters:
    sequence (list of int): The sequence of integers.

    Returns:
    int: The 1-based index of the first occurrence of the minimum value.
    """
    return sequence.index(min(sequence)) + 1