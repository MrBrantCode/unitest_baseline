"""
QUESTION:
Given a number N. We have to find maximum sum of all permutations of numbers from 1 to N. The maximum sum will be sum of absolute difference of adjacent elements in array.
Example 1:
Input: N = 2
Output: 1
Explaination: Permutations of 2 are: 
{1, 2} = 1, {2, 1} = 1.
Example 2:
Input: N = 3
Output: 3
Explaintation: Permutations of size 3 are: 
{1, 2, 3} = 1 + 1, {1, 3, 2} = 2 + 1 
{2, 1, 3} = 1 + 2, {2, 3, 1} = 1 + 2 
{3, 1, 2} = 2 + 1, {3, 2, 1} = 1 + 1 
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxSum() which takes N as input parameter and returns the maximum possible difference sum from all permutations of N numbers.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
2 ≤ N ≤ 1000
"""

def max_sum_of_permutations(N: int) -> int:
    if N == 1:
        return 1
    return N * (N - 1) // 2 + N // 2 - 1