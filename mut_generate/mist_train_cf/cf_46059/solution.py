"""
QUESTION:
Create a function named `minimal_distinctive` that takes two strings `input1` and `input2` as parameters. This function should return the longest common subsequence of `input1` and `input2`, which is a subset of characters positioned in the same order within both strings. The function should be case sensitive and should not modify the original order of characters in the input strings.
"""

def minimal_distinctive(input1, input2):
    # the dp table will have len(input1) + 1 rows and len(input2) + 1 columns.
    dp = [[None]*(len(input2)+1) for i in range(len(input1)+1)]
 
    # initialize the first row and first column as 0.
    for i in range(len(input1) + 1):
        for j in range(len(input2) + 1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif input1[i-1] == input2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
 
    # the value of the bottom right corner of the matrix
    # is the length of the LCS.
    lcs_length = dp[len(input1)][len(input2)]
 
    # Create a character array to store the lcs string
    lcs = [''] * (lcs_length+1)
    lcs[lcs_length] = ''

    # Start from the right-most bottom-most corner and
    # one by one store characters in lcs[]
    i = len(input1)
    j = len(input2)
    while i > 0 and j > 0:

        # If current character in input1 and input2 are same,
        # then current character is part of LCS
        if input1[i-1] == input2[j-1]:
            lcs[lcs_length-1] = input1[i-1]
            i-=1
            j-=1
            lcs_length-=1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
 
    lcs_string = "".join(lcs)
    return lcs_string