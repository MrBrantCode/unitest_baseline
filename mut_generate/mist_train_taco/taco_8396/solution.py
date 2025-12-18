"""
QUESTION:
There is an integer sequence A of length N whose values are unknown.
Given is an integer sequence B of length N-1 which is known to satisfy the following:
 B_i \geq \max(A_i, A_{i+1}) 
Find the maximum possible sum of the elements of A.

-----Constraints-----
 - All values in input are integers.
 - 2 \leq N \leq 100
 - 0 \leq B_i \leq 10^5

-----Input-----
Input is given from Standard Input in the following format:
N
B_1 B_2 ... B_{N-1}

-----Output-----
Print the maximum possible sum of the elements of A.

-----Sample Input-----
3
2 5

-----Sample Output-----
9

A can be, for example, ( 2 , 1 , 5 ), ( -1 , -2 , -3 ), or ( 2 , 2 , 5 ). Among those candidates, A = ( 2 , 2 , 5 ) has the maximum possible sum.
"""

def max_possible_sum_of_A(N: int, B: list) -> int:
    """
    Calculate the maximum possible sum of the elements of sequence A given the constraints.

    Parameters:
    - N (int): The length of the sequence A.
    - B (list): The sequence B of length N-1, where B_i >= max(A_i, A_{i+1}).

    Returns:
    - int: The maximum possible sum of the elements of A.
    """
    sumA = B[0] + B[N - 2]
    for i in range(N - 2):
        sumA += min(B[i], B[i + 1])
    return sumA