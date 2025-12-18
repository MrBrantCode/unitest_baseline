"""
QUESTION:
Implement a function `damerau_levenshtein_distance` that takes two strings `word1` and `word2` as input and returns the Damerau-Levenshtein distance between them. The function should use a dynamic programming approach to calculate the distance, which is the minimum number of operations (insertions, deletions, substitutions, and transpositions) required to change one word into the other.
"""

def damerau_levenshtein_distance(word1, word2):
    """
    This function calculates the Damerau-Levenshtein distance between two words.
    
    The Damerau-Levenshtein distance is the minimum number of operations (insertions, deletions, substitutions, and transpositions) 
    required to change one word into the other.
    
    Parameters:
    word1 (str): The first word.
    word2 (str): The second word.
    
    Returns:
    int: The Damerau-Levenshtein distance between the two words.
    """
    
    # Create the matrix with dimensions (len(word1) + 1) x (len(word2) + 1)
    matrix = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    
    # Initialize the matrix with values representing the distances between the empty substring and each substring of the words
    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j
    
    # Iterate through each cell in the matrix
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # If word1[i-1] == word2[j-1], set the current cell value to the value in the diagonal cell
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            # If word1[i-1] != word2[j-1], set the current cell value to the minimum of the possible operations
            else:
                substitution = matrix[i-1][j-1] + 1
                insertion = matrix[i][j-1] + 1
                deletion = matrix[i-1][j] + 1
                # Consider transposition if i and j are both greater than 1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]
                if i > 1 and j > 1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                    transposition = matrix[i-2][j-2] + 1
                    matrix[i][j] = min(substitution, insertion, deletion, transposition)
                else:
                    matrix[i][j] = min(substitution, insertion, deletion)
    
    # The final value in the bottom-right cell is the Damerau-Levenshtein distance between the two words
    return matrix[-1][-1]