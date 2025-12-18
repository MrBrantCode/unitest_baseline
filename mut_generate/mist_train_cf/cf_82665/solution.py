"""
QUESTION:
Implement a function named `purge_evens` that takes a 2D array as input. This function should remove all integers that are divisible by 2 from the array, preserve the original structure, and replace non-integer types with a null value. It must handle uneven 2D arrays, report any potential errors, and be efficient for large arrays. If a row in the array is not a list, the function should replace it with a null value and print an error message. If an element in the array is not an integer, the function should replace it with a null value and print an informative message.
"""

def purge_evens(matrix):
    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            print(f"Invalid entry at index {i}, not a list.")
            matrix[i] = None
            continue
        for j, elem in enumerate(row):
            if not isinstance(elem, int):
                print(f"Non-integer type at index {(i, j)}, replacing with null.")
                row[j] = None
            elif elem % 2 == 0:
                row[j] = None
    return matrix