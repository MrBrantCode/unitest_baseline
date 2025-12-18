"""
QUESTION:
Write a function `countDistinctSubsequences(string)` to compute the cumulative count of distinct non-redundant subsequences in the given string sequence. The function should take a string `string` as input and return the cumulative count of distinct subsequences. The function should handle all possible ASCII characters in the string.
"""

def countDistinctSubsequences(string):
    n = len(string)
    
    # dp[i] is going to store count of distinct subsequences of length i.
    dp = [0 for _ in range(n + 1)]

    # Empty substring has only one subsequence
    dp[0] = 1

    # Initialize an array to store last positions of characters seen in 'string'
    last = [-1 for _ in range(256)]
    # ascii value of 'a' is 97, 'b' is 98 and 'c' is 99

    for i in range(1, n + 1):
        # Count without string[i-1]
        dp[i] = 2 * dp[i-1]

        # Check if current character is previously seen
        if last[ord(string[i-1])] != -1:
            dp[i] = dp[i] - dp[last[ord(string[i-1]) - 1]]

        last[ord(string[i-1])] = i

    return dp[n]