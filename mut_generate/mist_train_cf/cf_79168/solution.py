"""
QUESTION:
Write a function `tally_numbers` that takes a three-dimensional matrix as input and returns a dictionary where the keys are the unique numbers in the matrix and the values are the number of times each number appears in the matrix. The input matrix is a list of lists of lists of integers.
"""

def tally_numbers(matrix):
    # Initialize an empty dictionary to hold number counts
    tally = {}

    # Iterate over each element in the matrix
    for layer in matrix:
        for row in layer:
            for num in row:
                # If the number is already in the dictionary, increment its count
                # Otherwise, add it to the dictionary with a count of 1
                tally[num] = tally.get(num, 0) + 1

    # Return the tally dictionary
    return tally