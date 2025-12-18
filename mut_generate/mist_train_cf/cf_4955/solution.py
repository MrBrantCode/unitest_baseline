"""
QUESTION:
Write a function named `print_diagonal` that takes a 2D array as input and prints its elements diagonally from left to right. The array may contain non-integer elements, negative numbers, and may not be a perfect rectangle (i.e., each row may not have the same number of columns). If the array is empty, print "Array is empty." If a non-integer element is found, print "Invalid element found in the array." and skip it. Negative numbers should be printed enclosed in parentheses.
"""

def print_diagonal(arr):
    # Check if array is empty
    if len(arr) == 0:
        print("Array is empty.")
        return
    
    # Print elements diagonally
    max_columns = max(len(row) for row in arr)
    for j in range(max_columns):
        for i in range(len(arr)):
            row = arr[i]
            if j < len(row) and i < len(arr[j]):
                element = arr[i][j]
                if not isinstance(element, int):
                    print("Invalid element found in the array.")
                elif element < 0:
                    print(f"({element})", end=" ")
                else:
                    print(element, end=" ")
        print()