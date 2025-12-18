"""
QUESTION:
You are given an array A of length N. Your task is to divide it into several contiguous subarrays. Here, all subarrays obtained must be sorted in either non-decreasing or non-increasing order. At least how many subarrays do you need to divide A into?

Constraints

* 1 \leq N \leq 10^5
* 1 \leq A_i \leq 10^9
* Each A_i is an integer.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the minimum possible number of subarrays after division of A.

Examples

Input

6
1 2 3 2 2 1


Output

2


Input

9
1 2 1 2 1 2 1 2 1


Output

5


Input

7
1 2 3 2 1 999999999 1000000000


Output

3
"""

def min_subarrays_to_divide(A: list) -> int:
    """
    Given an array A, this function calculates the minimum number of contiguous subarrays
    that can be formed such that each subarray is sorted in either non-decreasing or
    non-increasing order.

    Parameters:
    A (list): The input array of integers.

    Returns:
    int: The minimum number of subarrays required.
    """
    N = len(A)
    if N == 0:
        return 0
    
    sgn = 0
    answer = 1
    
    for i in range(N - 1):
        cur = A[i + 1] - A[i]
        if cur * sgn < 0:
            answer += 1
            sgn = 0
            continue
        if cur != 0:
            sgn = cur
    
    return answer