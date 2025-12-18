"""
QUESTION:
Create a function `longest_common_contiguous(b1, b2)` that takes two binary strings `b1` and `b2` as input and returns the longest contiguous series that occurs in both strings. The function should be able to handle any two binary strings `b1` and `b2` of any length.
"""

def longest_common_contiguous(b1, b2):
    len1 = len(b1)
    len2 = len(b2)
    
    # Create a 2D array to store the results
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    
    result = 0  # To store the length of the longest common contiguous series
    end = 0  # To store the ending point of the longest common contiguous series in b1

    # Fill dp[][]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if b1[i - 1] == b2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update result
                if dp[i][j] > result:
                    result = dp[i][j]
                    end = i - 1
            else:
                dp[i][j] = 0
                
    # The longest common contiguous series
    return b1[end - result + 1 : end + 1]