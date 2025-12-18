"""
QUESTION:
Write a function `print_diagonal(arr)` that prints the elements of a given two-dimensional array diagonally from left to right. The function should handle cases where the array is empty, not a perfect rectangle, contains non-integer elements, or contains negative numbers. If the array is empty, it should print "Array is empty." If the array contains non-integer elements, it should print an error message and skip those elements. Negative numbers should be printed enclosed in parentheses.
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
            if j < len(row):
                element = row[j]
                if not isinstance(element, int):
                    print("Invalid element found in the array.")
                elif element < 0:
                    print(f"({element})", end=" ")
                else:
                    print(element, end=" ")
        print()