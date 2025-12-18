"""
QUESTION:
Implement a function called `damerau_levenshtein_distance` that calculates the Damerau-Levenshtein Distance between two strings. The function should have a time complexity of O(m*n), where m is the length of the first string and n is the length of the second string. The function should handle cases where either string is empty and where the strings contain special characters. The Damerau-Levenshtein Distance allows for four types of operations: insertion, deletion, substitution, and transposition, where transposition is defined as swapping two adjacent characters in a string. The function should return the minimum number of operations required to transform the first string into the second string.
"""

def damerau_levenshtein_distance(str1, str2):
    # Handle case where either str1 or str2 is empty
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Create a matrix of size (len(str1)+1) x (len(str2)+1)
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Initialize the first row and first column of the matrix
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            
            # Calculate the minimum cost from three adjacent cells
            deletion = matrix[i-1][j] + 1
            insertion = matrix[i][j-1] + 1
            substitution = matrix[i-1][j-1] + cost
            matrix[i][j] = min(deletion, insertion, substitution)
            
            # Check for transposition operation
            if i > 1 and j > 1 and str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
                transposition = matrix[i-2][j-2] + cost
                matrix[i][j] = min(matrix[i][j], transposition)
    
    # Return the final value in the bottom right cell of the matrix
    return matrix[len(str1)][len(str2)]