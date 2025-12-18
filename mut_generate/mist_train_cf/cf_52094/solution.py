"""
QUESTION:
Write a function `max_identical_subsequence(s, t)` to find the maximal length of the identical subsequence shared by two strings `s` and `t`, where the subsequence elements must maintain their relative order in both strings. The function should not use built-in string comparison library functions and should be optimized for large strings with a length of up to 10⁴ characters. The function should return the length of the longest common subsequence.
"""

def max_identical_subsequence(s, t):
    length_s = len(s)
    length_t = len(t)
    
    # Initialize a DP table
    dp_table = [[0]*(length_t+1) for _ in range(length_s+1)]
    
    # Populate the DP table
    for i in range(1, length_s+1):
        for j in range(1, length_t+1):
            if s[i-1] == t[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
                
    return dp_table[-1][-1]