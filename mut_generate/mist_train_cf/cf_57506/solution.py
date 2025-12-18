"""
QUESTION:
Implement a function `min_edit_distance(str1, str2)` that calculates the minimum string edit distance between two strings. The strings can contain lowercase and uppercase alphabets, as well as numerical digits. The function should have a time complexity of O(m*n) and auxiliary space complexity of O(m*n), where m and n are the lengths of the input strings.
"""

def min_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store results of sub-problems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    # Fill dp[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If str1 is empty, only option is to
            # insert all characters of str2
            if i == 0:
                dp[i][j] = j 

            # If str2 is empty, only option is to
            # remove all characters of str1
            elif j == 0:
                dp[i][j] = i 

            # If last characters are same, ignore last character
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace
    return dp[m][n]