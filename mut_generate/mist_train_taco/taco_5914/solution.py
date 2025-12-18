"""
QUESTION:
Given an array A of N elements, find the number of distinct possible sums that can be obtained by taking any number of elements from the array and adding them.

Note that 0 can always be obtained by taking none.

First line of the input contains number of test cases T.
Each test case  has two lines. First line has N, the number of elements in the array followed by N values which are elements of the array.
For each test case, print a single line, the distinct possible sums that can be obtained.

Constraints
1 ≤ T ≤ 10 
1 ≤ N ≤ 100
0 ≤ A[i] ≤ 100 for 0 ≤ i < N

SAMPLE INPUT
3
3
1 2 3
5
5 1 3 2 7
4
1 2 4 8 

SAMPLE OUTPUT
7
19
16

Explanation

For the test case 1: Possible values are 0, 1, 2, 3, 4, 5, 6.
For the test case 2: All numbers between 0 and 18 inclusive.
For the test case 3: All numbers between 0 and 15 inclusive.
"""

def count_distinct_possible_sums(N: int, A: list) -> int:
    """
    Calculate the number of distinct possible sums that can be obtained by taking any number of elements from the array and adding them.

    Parameters:
    N (int): The number of elements in the array.
    A (list): The array of elements.

    Returns:
    int: The number of distinct possible sums.
    """
    if N == 0:
        return 1  # Only the sum 0 is possible if the array is empty
    
    sums = sum(A)
    dp = [[False] * (sums + 1) for _ in range(N)]
    dp[0][0] = True
    dp[0][A[0]] = True
    
    for i in range(1, N):
        for j in range(sums + 1):
            dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - A[i]] if j - A[i] >= 0 else False)
    
    return sum(dp[N - 1])