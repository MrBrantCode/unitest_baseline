"""
QUESTION:
> In information theory and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other.

(http://en.wikipedia.org/wiki/Levenshtein_distance)


Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.
"""

def calculate_levenshtein_distance(str1: str, str2: str) -> int:
    # Initialize the distance matrix
    d = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Fill the first row and first column of the matrix
    for i in range(len(str2) + 1):
        d[0][i] = i
    for i in range(len(str1) + 1):
        d[i][0] = i
    
    # Calculate the minimum edit distance
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            d[i + 1][j + 1] = min(
                1 + d[i][j + 1],  # Deletion
                1 + d[i + 1][j],  # Insertion
                d[i][j] + (1 if x != y else 0)  # Substitution
            )
    
    # The Levenshtein distance is the value in the bottom-right corner of the matrix
    return d[-1][-1]