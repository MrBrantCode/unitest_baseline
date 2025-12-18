"""
QUESTION:
Nikhil got to know about what is a matrice. He made several patterns using 1-d and 2-d matrices. One of which was his favorite pattern. Your task is to right a code for his favorite pattern.

NOTE :- To understand his favorite pattern see the sample output

Input:-

First line of code takes number of test cases 'N' as its input. The following N lines take size 'S' of a sqaure matrice as its input.

Output:-

Print Nikhils favorite pattern and seperate two different test cases with an empty line.

Constraint:-

N ≤ 10

S ≤ 10

SAMPLE INPUT
1
3

SAMPLE OUTPUT
123
894
765
"""

def generate_favorite_pattern(size):
    # total number of elements in array
    n = size * size
    
    # start at top left (row 0 column 0)
    row, column = 0, 0
    
    # first move is on the same row, to the right
    d_row, d_column = 0, 1
    
    # fill 2d array with dummy values we'll overwrite later
    arr = [[None] * size for _ in range(size)]
    
    for i in range(1, n + 1):
        arr[row][column] = i
        
        # next row and column
        nrow, ncolumn = row + d_row, column + d_column
        
        if 0 <= nrow < size and 0 <= ncolumn < size and arr[nrow][ncolumn] is None:
            # no out of bounds accesses or overwriting already-placed elements.
            row, column = nrow, ncolumn
        else:
            # change direction
            d_row, d_column = d_column, -d_row
            row, column = row + d_row, column + d_column
    
    return arr