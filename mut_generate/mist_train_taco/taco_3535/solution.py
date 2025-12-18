"""
QUESTION:
There are three houses on a number line: House 1, 2 and 3, with coordinates A, B and C, respectively. Print `Yes` if we pass the coordinate of House 3 on the straight way from House 1 to House 2 without making a detour, and print `No` otherwise.

Constraints

* 0\leq A,B,C\leq 100
* A, B and C are distinct integers.

Input

Input is given from Standard Input in the following format:


A B C


Output

Print `Yes` if we pass the coordinate of House 3 on the straight way from House 1 to House 2 without making a detour, and print `No` otherwise.

Examples

Input

3 8 5


Output

Yes


Input

7 3 1


Output

No


Input

10 2 4


Output

Yes


Input

31 41 59


Output

No
"""

def passes_house_three(a: int, b: int, c: int) -> str:
    if (c - a) * (c - b) < 0:
        return 'Yes'
    else:
        return 'No'