"""
QUESTION:
Create a function named `segregate_sort` that takes an array `arr` and an integer `n` as inputs. The function should remove duplicates from the array, sort the unique elements in descending order, and divide them into 'n' sections as evenly as possible. Each section should have a unique identifier. If 'n' is larger than the number of unique elements in the array, the function should return an error message.
"""

import numpy as np

def segregate_sort(arr, n):
    # Convert list to np.array
    arr = np.array(arr)
    # Remove duplicates & sort in descending
    arr = np.sort(np.unique(arr))[::-1]
    
    # If n is larger than unique elems, return error
    if n > len(arr):
        return "Error: 'n' is larger than the number of unique elements in the array."

    # Compile the final output
    output = {}
    div, mod = divmod(len(arr), n)
    for i in range(n):
        start_index = i * div
        end_index = start_index + div + (i < mod)
        output[i] = list(arr[start_index : end_index])

    return output