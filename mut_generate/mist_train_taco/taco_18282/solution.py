"""
QUESTION:
Given a sequence of numbers a1, a2, a3, ..., an, find the maximum sum of a contiguous subsequence of those numbers. Note that, a subsequence of one element is also a contiquous subsequence.



Input

The input consists of multiple datasets. Each data set consists of:


n
a1
a2
.
.
an


You can assume that 1 ≤ n ≤ 5000 and -100000 ≤ ai ≤ 100000.

The input end with a line consisting of a single 0.

Output

For each dataset, print the maximum sum in a line.

Example

Input

7
-5
-1
6
4
9
-6
-7
13
1
2
3
2
-2
-1
1
2
3
2
1
-2
1
3
1000
-200
201
0


Output

19
14
1001
"""

def max_subsequence_sum(sequence: list[int]) -> int:
    """
    Calculate the maximum sum of a contiguous subsequence from the given sequence of numbers.

    Parameters:
    sequence (list[int]): A list of integers representing the sequence of numbers.

    Returns:
    int: The maximum sum of a contiguous subsequence.
    """
    if not sequence:
        return 0
    
    mi = su = 0
    ans = -10 ** 9
    
    for num in sequence:
        su += num
        ans = max(ans, su - mi)
        mi = min(su, mi)
    
    return ans