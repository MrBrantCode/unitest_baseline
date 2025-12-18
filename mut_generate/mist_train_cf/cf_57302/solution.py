"""
QUESTION:
Write a function `edit_distance(string1, string2)` that calculates the minimum number of operations (insertions, deletions, or substitutions) required to transform `string1` into `string2` using dynamic programming. The function should take two strings as input and return the minimum edit distance.
"""

def edit_distance(string1, string2):
    # Length of two strings
    len_str1 = len(string1)
    len_str2 = len(string2)
    
    # Create a matrix of zeros with dimensions (len_str1+1, len_str2+1)
    dp = [[0 for x in range(len_str2+1)] for x in range(len_str1+1)]
    
    # Initialize the first column
    for i in range(len_str1+1):
        dp[i][0] = i
        
    # Initialize the first row
    for i in range(len_str2+1):
        dp[0][i] = i
        
    # Traverse through the matrix
    for i in range(1, len_str1+1):
        for j in range(1, len_str2+1):
            # If last characters of two strings are same, nothing much to do. Ignore last characters and get the count of remaining strings.
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If the last character is different, consider all possibilities (replace, remove, insert) and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace
    # Return min distance
    return dp[len_str1][len_str2]