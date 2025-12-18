"""
QUESTION:
Given a binary string S consisting of 0s and 1s. The task is to find the maximum difference of the number of 0s and the number of 1s (number of 0s – number of 1s) in the substrings of a string.
Note: In the case of all 1s, the answer will be -1. 
Example 1:
Input : S = "11000010001" 
Output : 6 
Explanatio: From index 2 to index 9, 
there are 7 0s and 1 1s, so number 
of 0s - number of 1s is 6. 
Example 2:
Input: S = "111111"
Output: -1
Explanation: S contains 1s only 
Your task:
You do not need to read any input or print anything. The task is to complete the function maxSubstring(), which takes a string as input and returns an integer. 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 10^{5}
S contains 0s and 1s only
"""

import numpy as np

def max_substring_difference(S: str) -> int:
    """
    Finds the maximum difference of the number of '0's and '1's in any substring of the input binary string.

    Parameters:
    S (str): The input binary string consisting of '0's and '1's.

    Returns:
    int: The maximum difference of the number of '0's and '1's in any substring of the input string.
         If the string consists entirely of '1's, returns -1.
    """
    n = len(S)
    dp = np.array([0] * (n + 1))
    
    for j in range(n):
        if S[j] == '1':
            dp[j + 1] = max(dp[j] - 1, -1)
        else:
            dp[j + 1] = max(dp[j] + 1, 1)
    
    return np.max(dp) if '0' in S else -1