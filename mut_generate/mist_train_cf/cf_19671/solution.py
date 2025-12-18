"""
QUESTION:
Write a function `print_column_wise(arr)` that takes a two-dimensional array `arr` as input and prints its elements column-wise. The function should handle the following cases: 

- If the array is empty, print "The array is empty."
- If the array is not a perfect rectangle, print an error message for each row with a different number of columns and skip that row while printing.
- If the array contains non-integer elements, print an error message for each non-integer element and skip that element while printing.

The array does not contain any nested arrays.
"""

def print_column_wise(arr):
    if not arr:  # Check if the array is empty
        print("The array is empty.")
        return
    
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    for j in range(num_cols):
        for i in range(num_rows):
            if len(arr[i]) != num_cols:  # Check if the row has the same number of columns as the first row
                print("Error: Row", i+1, "has a different number of columns.")
                break
            if not isinstance(arr[i][j], int):  # Check if the element is an integer
                print("Error: Element at position (", i+1, ",", j+1, ") is not an integer.")
                continue
            print(arr[i][j], end=" ")
        print()  # Print a new line after printing each column