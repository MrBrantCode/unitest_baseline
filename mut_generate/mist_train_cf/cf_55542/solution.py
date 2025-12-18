"""
QUESTION:
Write a function `check_descending_order(arr)` that checks if all elements in a given 4D array `arr` are in descending order. The function should return `True` if the array is in descending order and `False` otherwise. The array is in descending order if an element at `array[n][i][j][k]` is greater than or equal to elements at `array[m][p][q][r]` if `n>=m`, `i>=p`, `j>=q`, and `k>=r`, for all elements in the 4D array.
"""

def check_descending_order(arr):
    for n in range(len(arr)):
        for i in range(len(arr[n])):
            for j in range(len(arr[n][i])):
                for k in range(len(arr[n][i][j])):
                    for m in range(n+1):
                        for p in range(i+1):
                            for q in range(j+1):
                                for r in range(k+1):
                                    if n >= m and i >= p and j >= q and k >= r and arr[n][i][j][k] < arr[m][p][q][r]:
                                        return False
    return True