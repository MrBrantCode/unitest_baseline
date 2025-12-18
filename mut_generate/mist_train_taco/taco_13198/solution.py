"""
QUESTION:
We have a rectangular parallelepiped of size A×B×C, built with blocks of size 1×1×1. Snuke will paint each of the A×B×C blocks either red or blue, so that:

* There is at least one red block and at least one blue block.
* The union of all red blocks forms a rectangular parallelepiped.
* The union of all blue blocks forms a rectangular parallelepiped.



Snuke wants to minimize the difference between the number of red blocks and the number of blue blocks. Find the minimum possible difference.

Constraints

* 2≤A,B,C≤10^9

Input

The input is given from Standard Input in the following format:


A B C


Output

Print the minimum possible difference between the number of red blocks and the number of blue blocks.

Examples

Input

3 3 3


Output

9


Input

2 2 4


Output

0


Input

5 3 5


Output

15
"""

def min_difference_of_painted_blocks(A, B, C):
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        return 0
    else:
        return min(A * B, B * C, C * A)