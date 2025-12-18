"""
QUESTION:
We are given a N*M grid, print the number of rectangles in it modulo (10^{9}+7).
 
Example 1:
Input:
N = 2, M = 2
Output:
9
Explanation:
There are 4 rectangles of size 1 x 1
There are 2 rectangles of size 1 x 2
There are 2 rectangles of size 2 x 1
There is  1 rectangle of size 2 X 2.
Example 2:
Input:
N = 5, M = 4
Output:
150
Explanation:
There are a total of 150 rectangles.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function rectNum() which takes 2 Integers N and M as input and returns the number of rectangles in a N*M grid modulo (10^{9}+7).
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N,M <= 10^{4}
"""

def count_rectangles(N: int, M: int) -> int:
    MOD = 1000000007
    return int(N * M * (N + 1) * (M + 1) / 4 % MOD)