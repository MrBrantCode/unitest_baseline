"""
QUESTION:
There is a sequence of length N: A_1, A_2, ..., A_N. Initially, this sequence is a permutation of 1, 2, ..., N.
On this sequence, Snuke can perform the following operation:
 - Choose K consecutive elements in the sequence. Then, replace the value of each chosen element with the minimum value among the chosen elements.
Snuke would like to make all the elements in this sequence equal by repeating the operation above some number of times.
Find the minimum number of operations required.
It can be proved that, Under the constraints of this problem, this objective is always achievable.

-----Constraints-----
 - 2 \leq K \leq N \leq 100000
 - A_1, A_2, ..., A_N is a permutation of 1, 2, ..., N.

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 ... A_N

-----Output-----
Print the minimum number of operations required.

-----Sample Input-----
4 3
2 3 1 4

-----Sample Output-----
2

One optimal strategy is as follows:
 - In the first operation, choose the first, second and third elements. The sequence A becomes 1, 1, 1, 4.
 - In the second operation, choose the second, third and fourth elements. The sequence A becomes 1, 1, 1, 1.
"""

def minimum_operations_to_equalize(N: int, K: int, A: list) -> int:
    """
    Calculate the minimum number of operations required to make all elements in the sequence equal.

    Parameters:
    - N (int): The length of the sequence.
    - K (int): The number of consecutive elements that can be chosen in one operation.
    - A (list): The sequence of integers.

    Returns:
    - int: The minimum number of operations required.
    """
    if N == K:
        return 1
    else:
        operations = 1
        N -= K
        while N > 0:
            operations += 1
            N -= (K - 1)
        return operations