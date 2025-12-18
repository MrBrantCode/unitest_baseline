"""
QUESTION:
You'll be given an array A of N integers as input. For each element of the array A[i], print A[i]-1. 

Input:
There will be N+1 iines of input each consisting of a single integer.
Integer in first line denotes N
For the following N lines the integer in i^{th} line denotes the integer A[i-1]

Output:
For each element of the array A[i], print A[i]-1 in a new line.

Constraints:
1 ≤ N ≤ 10 
1 ≤ A[i] ≤ 10  

SAMPLE INPUT
2
2
6

SAMPLE OUTPUT
1
5
"""

def compute_decremented_values(A: list[int]) -> list[int]:
    """
    Computes a new list where each element is the corresponding element in the input list decremented by 1.

    Parameters:
    A (list[int]): The input list of integers.

    Returns:
    list[int]: A list of integers where each element is A[i] - 1.
    """
    return [x - 1 for x in A]