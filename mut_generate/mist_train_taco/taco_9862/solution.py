"""
QUESTION:
Pandu has started learning about sub-sets. His teacher gave him a simple work. Given a list of numbers, Pandu has to choose the sub-set which gives the max product. However, the teacher asked Pandu only to submit the max product obtained by taking exactly two numbers from the list. Please help Pandu in finding out the answer to this assignment.

Input Format:

The first line will contain the integer N, the length of the array. The next line contains N space separated integers.

Output Format:

For each test case, output Pandu's query.

Constraints:

2 ≤ N ≤ 105

Subtask 1: (25 points)
0 ≤ Integers ≤ 109

Subtask 2: (75 points)
-109 ≤ Integers ≤ 109

SAMPLE INPUT
2
2 3

SAMPLE OUTPUT
6
"""

def max_product_of_two(arr):
    """
    Calculate the maximum product of exactly two numbers from the given list.

    Parameters:
    arr (list of int): The list of integers.

    Returns:
    int: The maximum product of two numbers from the list.
    """
    arr.sort()
    neg = arr[0] * arr[1]
    pos = arr[-1] * arr[-2]
    return max(neg, pos)