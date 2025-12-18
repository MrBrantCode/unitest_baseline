"""
QUESTION:
Write a function `DSM_to_number` that takes a diamond-shaped matrix (`dsm`) of integers as input, represented as a list of lists, and returns a single integer formed by concatenating all the integers in the matrix. The input matrix is guaranteed to be a diamond shape, but its size and values are arbitrary. The output integer should be formed by concatenating the integers in the order they appear in the input matrix.
"""

def DSM_to_number(dsm):
    # Flatten the diamond shaped matrix and join elements into a string
    s = ''.join(str(i) for row in dsm for i in row)
    # Convert the string to an integer and return
    return int(s)