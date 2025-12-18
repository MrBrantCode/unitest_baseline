"""
QUESTION:
Given a binary string S consists only of 0s and 1s. The task is to calculate the number of substrings that have more 1s than 0s.
Example 1:
Input:
S = "011"
Output: 4
Explanation: There are 4 substring which 
has more 1s than 0s. i.e "011","1","11" and "1"
Example 2:
Input:
S = "0000"
Output: 0
Explanation: There is no substring
which has more 1s than 0s
Your Task:  
You dont need to read input or print anything. Complete the function countSubstring() which takes the string S as input parameter and returns the number of substring which has more 1s than 0s.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
Constraints:
1 < |S| < 10^{5}
|S| denotes the length of the string S
"""

def count_substrings_with_more_ones(S: str) -> int:
    n = len(S)
    dp = [0] * (2 * n + 1)
    minius, count = 0, n
    
    for i in range(n):
        if S[i] == '0':
            count -= 1
        else:
            count += 1
        if count <= n:
            minius += 1
        dp[count] += 1
    
    ans = 0
    ind = n
    
    for i in range(n):
        ans += n - i - minius
        if S[i] == '1':
            ind += 1
            dp[ind] -= 1
            minius += dp[ind]
        else:
            minius -= 1
            minius -= dp[ind]
            ind -= 1
            dp[ind] -= 1
    
    return ans