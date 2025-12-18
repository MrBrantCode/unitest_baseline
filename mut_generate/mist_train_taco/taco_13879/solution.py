"""
QUESTION:
Find the intersection of two sets $A = \\{a_0, a_1, ..., a_{n-1}\\}$ and $B = \\{b_0, b_1, ..., b_{m-1}\\}$.

Constraints

* $1 \leq n, m \leq 200,000$
* $0 \leq a_0 < a_1 < ... < a_{n-1} \leq 10^9$
* $0 \leq b_0 < b_1 < ... < b_{m-1} \leq 10^9$

Input

The input is given in the following format.


$n$
$a_0 \; a_1 \; ... \; a_{n-1}$
$m$
$b_0 \; b_1 \; ... \; b_{m-1}$


Elements of $A$ and $B$ are given in ascending order respectively. There are no duplicate elements in each set.

Output

Print elements in the intersection in ascending order. Print an element in a line.

Example

Input

4
1 2 5 8
5
2 3 5 9 11


Output

2
5
"""

def find_intersection(set_a: list, set_b: list) -> list:
    """
    Find the intersection of two sets A and B.

    Parameters:
    set_a (list): A list of integers representing the first set.
    set_b (list): A list of integers representing the second set.

    Returns:
    list: A list of integers representing the intersection of set_a and set_b.
    """
    return sorted(set(set_a) & set(set_b))