"""
QUESTION:
Description
IIT Gandhinagar has a strong policy against plagiarism. The institute decides to develop a program that measures how different two texts are from each other. Suppose there are two text strings A and B, the program should be able to calculate the minimum number of characters that must be added to and/or removed from A to get B, called Dissimilarity (or equivalently, the total
numbers of characters that must be added to A and B to make them equal).

Input Format
First line contains A
Second line contains B

Output Format
One line containing the Dissimilarity of A to B

Input Limits
0 < Length(A), Length(B) < 200

SAMPLE INPUT
written word
kitten purred

SAMPLE OUTPUT
9

Explanation

For example if A is "written word" and B is "kitten purred" we can delete 4 characters from A to get "itten rd" and then add 5 new ones(k,p,u,r,e) to get B, such that the total number of characters added or removed from A to get B count to 9. Therefore we define the Dissimilarity of A from B to be 9.

You are required to write the program to compute the dissimilarity of two texts.
"""

def calculate_dissimilarity(A: str, B: str) -> int:
    """
    Calculate the dissimilarity between two text strings A and B.
    The dissimilarity is defined as the minimum number of characters
    that must be added to and/or removed from A to get B.

    Parameters:
    A (str): The first text string.
    B (str): The second text string.

    Returns:
    int: The dissimilarity between A and B.
    """
    m = len(A)
    n = len(B)
    
    # Create a 2D array to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    
    # Fill dp array
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Min. operations = j
            elif j == 0:
                dp[i][j] = i  # Min. operations = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j])  # Remove
    
    return dp[m][n]