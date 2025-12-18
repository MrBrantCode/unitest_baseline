"""
QUESTION:
Find the difference of two sets $A = \\{a_0, a_1, ..., a_{n-1}\\}$ and $B = \\{b_0, b_1, ..., b_{m-1}\\}$, $A - B$.

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


Elements in $A$ and $B$ are given in ascending order. There are no duplicate elements in each set.

Output

Print elements in the difference in ascending order. Print an element in a line.

Example

Input

5
1 2 3 5 8
2
2 5


Output

1
3
8
"""

def set_difference(set_a: set, set_b: set) -> list:
    """
    Compute the difference of two sets A and B, i.e., A - B.

    Parameters:
    set_a (set): The first set.
    set_b (set): The second set.

    Returns:
    list: A list of elements in the difference set_a - set_b, sorted in ascending order.
    """
    return sorted(list(set_a - set_b))