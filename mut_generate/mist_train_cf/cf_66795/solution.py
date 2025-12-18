"""
QUESTION:
Define a function `LCIS(X, Y)` that takes two integer sequences `X` and `Y` as input and returns the length of the longest common increasing subsequence present in both sequences. The subsequence should be strictly increasing, meaning all elements are in ascending order. Assume both sequences contain distinct elements and may be empty, but will not be `None`.
"""

def findLengthOfLCIS(X, Y):
    m = len(X)
    n = len(Y)
  
    # table to store lengths of longest 
    # common suffixes of substrings.
    t = [[0 for i in range(n+1)] 
            for i in range(m+1)] 
  
    res = 0  # To store length of result
  
    # Building table in bottom-up manner 
    for i in range(1, m+1): 
        current = 0
        for j in range(1, n+1): 
            if (X[i - 1] == Y[j - 1]): 
                t[i][j] = current + 1
                res = max(res, t[i][j])
            elif (X[i - 1] > Y[j - 1]): 
                current = max(current, t[i][j])
  
    # Length of result
    return res 