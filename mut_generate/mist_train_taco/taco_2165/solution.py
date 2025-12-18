"""
QUESTION:
For a sequence of integers $A = \\{a_0, a_1, ..., a_{n-1}\\}$ which is sorted by ascending order, eliminate all equivalent elements.

Constraints

* $1 \leq n \leq 100,000$
* $-1000,000,000 \leq a_i \leq 1,000,000,000$
* $a_0 \leq a_1 \leq ... \leq a_{n-1}$

Input

A sequence is given in the following format.


$n$
$a_0 \; a_1 \; ,..., \; a_{n-1}$


Output

Print the sequence after eliminating equivalent elements in a line. Separate adjacency elements by a space character.

Example

Input

4
1 2 2 4


Output

1 2 4
"""

def remove_duplicates_from_sorted_array(arr):
    """
    Removes duplicate elements from a sorted list of integers.

    Parameters:
    arr (list of int): A sorted list of integers.

    Returns:
    list of int: A list of integers with duplicate elements removed.
    """
    return sorted(set(arr))