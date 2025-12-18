"""
QUESTION:
Write a function called `print_column_wise` that takes a 2D array as input and prints its elements column-wise. The function should handle cases where the array is empty, rows have different lengths, and non-integer elements are present. If the array is empty, the function should print "The array is empty." If a row has a different length than the first row, the function should print an error message and skip that row. If an element is not an integer, the function should print an error message and skip that element.
"""

def print_column_wise(arr):
    if not arr:  
        print("The array is empty.")
        return
    
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    for j in range(num_cols):
        for i in range(num_rows):
            if len(arr[i]) != num_cols:  
                print("Error: Row", i+1, "has a different number of columns.")
                break
            if not isinstance(arr[i][j], int):  
                print("Error: Element at position (", i+1, ",", j+1, ") is not an integer.")
                continue
            print(arr[i][j], end=" ")
        print()  