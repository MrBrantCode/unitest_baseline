"""
QUESTION:
You are given an integer sequence A of length N.
Find the maximum absolute difference of two elements (with different indices) in A.

-----Constraints-----
 - 2 \leq N \leq 100
 - 1 \leq A_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 A_2 ... A_N

-----Output-----
Print the maximum absolute difference of two elements (with different indices) in A.

-----Sample Input-----
4
1 4 6 3

-----Sample Output-----
5

The maximum absolute difference of two elements is A_3-A_1=6-1=5.
"""

def max_absolute_difference(A: list[int]) -> int:
    """
    Calculate the maximum absolute difference between any two elements in the list A.

    Parameters:
    A (list[int]): A list of integers.

    Returns:
    int: The maximum absolute difference between any two elements in the list A.
    """
    ans = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(abs(A[i] - A[j]), ans)
    return ans