"""
QUESTION:
Given the mobile numeric keypad. You can only press buttons that are up, left, right, or down to the current button or the current button itself (like 00,11, etc.). You are not allowed to press the bottom row corner buttons (i.e. * and # ). Given a number N, the task is to find out the number of possible numbers of the given length.
Example 1:
Input: 1
Output: 10
Explanation: Number of possible numbers 
would be 10 (0, 1, 2, 3, ., 9)  
Example 2:
Input: N = 2
Output: 36
Explanation: Possible numbers: 00, 08, 11,
12, 14, 22, 21, 23, 25 and so on.
If we start with 0, valid numbers 
will be 00, 08 (count: 2)
If we start with 1, valid numbers 
will be 11, 12, 14 (count: 3)
If we start with 2, valid numbers 
will be 22, 21, 23,25 (count: 4)
If we start with 3, valid numbers 
will be 33, 32, 36 (count: 3)
If we start with 4, valid numbers 
will be 44,41,45,47 (count: 4)
If we start with 5, valid numbers 
will be 55,54,52,56,58 (count: 5) 
and so on..
Your Task:  
You don't need to read input or print anything. Complete the function getCount() which takes N as input parameter and returns the integer value
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 25
"""

def count_possible_numbers(N: int) -> int:
    # Define the neighbors for each key on the numeric keypad
    neigh = [
        [0, 8], [1, 2, 4], [1, 2, 3, 5], [2, 3, 6], [1, 4, 5, 7],
        [2, 4, 5, 6, 8], [3, 5, 6, 9], [4, 7, 8], [5, 7, 8, 9, 0], [6, 8, 9]
    ]
    
    # Initialize the dp and ans arrays
    dp = [-1 for _ in range(10)]
    ans = [1 for _ in range(10)]
    
    # Calculate the number of possible numbers for each length from 2 to N
    for n in range(2, N + 1):
        for k in range(10):
            res = 0
            for i in neigh[k]:
                res += ans[i]
            dp[k] = res
        ans = dp[:]
        dp = [-1 for _ in range(10)]
    
    # Return the sum of possible numbers of length N
    return sum(ans)