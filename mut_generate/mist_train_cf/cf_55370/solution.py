"""
QUESTION:
Write a function called `calculate_array` that accepts a multi-dimensional array as input. The function should print the contents of the array and calculate the number of rows and columns. If the array is rectangular (non-ragged), the function should also calculate and print the transpose of the array. For 2D rectangular arrays, the function should include an option to print the array in a spiral order. The function should handle ragged arrays without throwing an error, skipping the transpose operation in such cases.
"""

import numpy as np

def calculate_array(arr):
    try:
        np_arr = np.array(arr)
    except:
        print("An error occurred while creating the numpy array.")
        return

    print("Array contents:")
    print(np_arr)

    shape = np_arr.shape
    if len(shape) < 2:
        print(f"The array has {shape[0]} rows.")
        print(f"The array has 1 column.")
    else:
        print(f"The array has {shape[0]} rows.")
        print(f"The array has {shape[1]} columns.")

        try:
            transpose = np_arr.T
            print("\nTransposed array:")
            print(transpose)

            while np_arr.size:
                for x in np_arr[0]:
                    print(x, end = ' ')
                np_arr = np_arr[1:].T[::-1]
            print()
        except:
            print("The array is ragged, so transpose operation was skipped.")