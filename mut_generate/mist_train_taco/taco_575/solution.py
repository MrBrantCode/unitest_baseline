"""
QUESTION:
Given a set of m distinct positive integers and a value ‘N’. Count the total number of ways we can form ‘N’ by  adding the array elements. Repetitions and different arrangements are allowed.
Note: Answer can be quite large output the answer modulo 10^{9}+7.
Example 1:
Input:
m = 3 , N = 7
Arr[] = {1,5,6}
Output: 6
Explanation: The different ways are:
1+1+1+1+1+1+1
1+1+5
1+5+1
5+1+1
1+6
6+1
Ã¢â¬â¹Example 2:
Input: 
m = 3 , N = 3
Arr[] = {1,2,3}
Output: 4
Explanation: The different ways are:
1+1+1
1+2
2+1
3  
Your Task:
You don't need to read input or print anything. Your task is to complete the function countWays() which accepts array arr[], its size m and integer N and returns the total number of ways we can form ‘N’ by adding array elements.
Expected Time Complexity: O(N*m)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N , m <= 10^{3}
"""

def count_ways(arr, m, N):
    # Sort the array to handle smaller numbers first
    arr.sort()
    
    # Initialize a dp array where dp[i] represents the number of ways to form sum i
    dp = [0] * (N + 1)
    dp[0] = 1  # There's one way to form the sum 0, which is using no elements
    
    # Fill the dp array
    for total in range(1, N + 1):
        for num in arr:
            if total - num >= 0:
                dp[total] += dp[total - num]
    
    # Return the result modulo 10^9 + 7
    return dp[N] % (10**9 + 7)