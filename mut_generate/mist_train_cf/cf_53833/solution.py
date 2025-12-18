"""
QUESTION:
Write a function named `bubble_sort` that sorts an array of strings in descending order using the Bubble Sort algorithm, without utilizing Python's built-in sorting functions. The sorting should be case-insensitive but preserve the original casing of the strings in the output. Numerical strings should be handled as their respective numerical values for sorting purposes, rather than being treated alphabetically. The input array may contain a mix of strings with and without numerical prefixes.
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            j_val = arr[j].lower()
            j_PlusOne_val = arr[j+1].lower()

            if j_val.isnumeric() and j_PlusOne_val.isnumeric():
                # Compare the values as Integers
                if int(j_val) < int(j_PlusOne_val):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif j_val.isnumeric():
                continue
            elif j_PlusOne_val.isnumeric():
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif j_val < j_PlusOne_val:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr