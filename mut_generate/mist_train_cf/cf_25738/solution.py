"""
QUESTION:
Create a function `is_nearly_identical(str1, str2)` that checks whether two input strings are nearly identical, meaning they differ by at most one edit operation (insertion, deletion, or substitution). The function should return True if the strings are nearly identical, and False otherwise.
"""

def is_nearly_identical(str1, str2): 
    """
    Checks whether two input strings are nearly identical, 
    meaning they differ by at most one edit operation (insertion, deletion, or substitution).
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        bool: True if the strings are nearly identical, False otherwise.
    """

    m = len(str1)
    n = len(str2)

    # Create matrix to store results of  subproblems 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    for i in range(m + 1): 
        for j in range(n + 1):  
            if i == 0: 
                dp[i][j] = j   
            elif j == 0: 
                dp[i][j] = i    
            elif str1[i - 1] == str2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j - 1],      # Insert 
                                   dp[i - 1][j],      # Remove 
                                   dp[i - 1][j - 1])  # Replace 

    return dp[m][n] <= 1