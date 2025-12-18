"""
QUESTION:
Implement a function `product_of_coords(multi_list)` that takes a multi-dimensional list of integers as input. The function should return the product of all the elements at coordinates where the product of the row index and column index (1-based indexing) is an odd number. Assume all row and column indices are positive integers and all values in the list are between 1 and 1000.
"""

def product_of_coords(multi_list): 
    result = 1
    row_length = len(multi_list)
    if row_length > 0:
        col_length = len(multi_list[0])
        for i in range(row_length):
            for j in range(col_length):
                # increment i and j by 1 as we're considering 1-based index
                if ((i+1) * (j+1)) % 2 == 1:
                    result *= multi_list[i][j]
    return result