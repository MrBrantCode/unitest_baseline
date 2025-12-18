"""
QUESTION:
Roman has no idea, why this problem is called Stone. He also has no idea on how to solve the followong problem: given array of N integers A and a number K. During a turn the maximal value over all Ai is chosen, let's call it MAX. Then Ai = 
MAX - Ai is done for every 1 <= i <= N. Help Roman to find out how will the array look like after K turns.

-----Input-----
The numbers N and K are given in the first line of an input. Then N integers are given in the second line which denote the array A. 

-----Output-----
Output N numbers on a single line. It should be the array A after K turns.

-----Constraints-----

- 1 <= N <= 105
- 0 <= K <= 109
- Ai does not exceed 2 * 109 by it's absolute value.

-----Example-----
Input:
4 1
5 -1 7 0

Output:
2 8 0 7
"""

def transform_array_after_k_turns(N: int, K: int, A: list) -> list:
    """
    Transforms the array A after K turns according to the given problem statement.

    Parameters:
    - N (int): The number of integers in the array.
    - K (int): The number of turns.
    - A (list): The array of integers.

    Returns:
    - list: The transformed array after K turns.
    """
    if K == 0:
        return A
    
    maximum = max(A)
    minimum = min(A)
    
    if K % 2 == 1:
        return [maximum - i for i in A]
    else:
        return [i - minimum for i in A]