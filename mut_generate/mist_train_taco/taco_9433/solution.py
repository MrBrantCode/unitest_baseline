"""
QUESTION:
You are given a sequence of n integers S and a sequence of different q integers T. Write a program which outputs C, the number of integers in T which are also in the set S.

Notes

Constraints

* Elements in S is sorted in ascending order
* n ≤ 100000
* q ≤ 50000
* 0 ≤ an element in S ≤ 109
* 0 ≤ an element in T ≤ 109

Input

In the first line n is given. In the second line, n integers are given. In the third line q is given. Then, in the fourth line, q integers are given.

Output

Print C in a line.

Examples

Input

5
1 2 3 4 5
3
3 4 1


Output

3


Input

3
1 2 3
1
5


Output

0


Input

5
1 1 2 2 3
2
1 2


Output

2
"""

import bisect

def count_common_elements(S, T):
    """
    Counts the number of integers in T that are also in the set S.

    Parameters:
    S (list of int): A sorted list of integers.
    T (list of int): A list of integers to check against S.

    Returns:
    int: The count of integers in T that are also in S.
    """
    ans = 0
    for t in T:
        x = bisect.bisect_left(S, t)
        if x < len(S) and S[x] == t:
            ans += 1
    return ans