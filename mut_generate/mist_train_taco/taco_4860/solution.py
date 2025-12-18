"""
QUESTION:
Given an array of N integers, using ‘+’ and ‘-‘ between the elements check if there is a way to form a sequence of numbers that evaluates a number divisible by M.
 
Example 1:
Ã¢â¬â¹Input : arr[ ] = {1, 2, 3, 4, 6} and M = 4
Output : 1
Explanation:
There is a valid sequence i. e., 
(1 - 2 + 3 + 4 + 6), which evaluates to 12 
that is divisible by 4.
Example 2:
Input : arr[ ] = {1, 3, 9} 
Output :  0 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function validSequence() that takes an array (arr), sizeOfArray (n), an integer M and return the true if there is a way to form a sequence of numbers which evaluate to a number divisible by M else return false. The driver code takes care of the printing.
Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M).
 
Constraints:
1 ≤ N < 1000
1 ≤ M <1000
"""

def validSequence(arr, n, m):
    dp = []
    for i in range(n + 1):
        dp.append([-1] * m)

    def recur(i, arr, n, m, su):
        if i == n:
            if su == 0:
                return True
            else:
                return False
        if dp[i][su] != -1:
            return dp[i][su]
        val1 = recur(i + 1, arr, n, m, (su + arr[i]) % m)
        val2 = recur(i + 1, arr, n, m, (su - arr[i]) % m)
        dp[i][su] = val1 or val2
        return dp[i][su]
    
    return recur(0, arr, n, m, 0)