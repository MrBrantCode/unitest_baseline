"""
QUESTION:
Given two integers m & n, find the number of possible sequences of length n such that each of the next element is greater than or equal to twice of the previous element but less than or equal to m.
Example 1:
Input: m = 10, n = 4
Output: 4
Explaination: There should be n elements and 
value of last element should be at-most m. 
The sequences are {1, 2, 4, 8}, {1, 2, 4, 9}, 
{1, 2, 4, 10}, {1, 2, 5, 10}.
Example 2:
Input: m = 5, n = 2
Output: 6
Explaination: The sequences are {1, 2}, 
{1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}.
Your Task:
You do not need to read input or print anything. Your task is to complete the function numberSequence() which takes the number m and n as input parameters and returns the number of sequences.
Expected Time Complexity: O(m*n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ m, n ≤ 100
"""

def count_valid_sequences(m: int, n: int) -> int:
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1] = [1] * (m + 1)
    
    for seq in range(2, n + 1):
        for num in range(1, m + 1):
            if num < seq:
                dp[seq][num] = 0
            else:
                dp[seq][num] = sum(dp[seq - 1][1:num // 2 + 1])
    
    return sum(dp[n])