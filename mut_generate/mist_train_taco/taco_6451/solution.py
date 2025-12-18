"""
QUESTION:
Given is a sequence of integers A_1, A_2, ..., A_N.
If its elements are pairwise distinct, print YES; otherwise, print NO.

-----Constraints-----
 - 2 ≤ N ≤ 200000
 - 1 ≤ A_i ≤ 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 ... A_N

-----Output-----
If the elements of the sequence are pairwise distinct, print YES; otherwise, print NO.

-----Sample Input-----
5
2 6 1 4 5

-----Sample Output-----
YES

The elements are pairwise distinct.
"""

def are_elements_pairwise_distinct(N: int, A: list) -> str:
    """
    Determines if the elements in the sequence are pairwise distinct.

    Parameters:
    - N (int): The number of elements in the sequence.
    - A (list): A list of integers representing the sequence.

    Returns:
    - str: "YES" if the elements are pairwise distinct, otherwise "NO".
    """
    return "YES" if len(set(A)) == N else "NO"