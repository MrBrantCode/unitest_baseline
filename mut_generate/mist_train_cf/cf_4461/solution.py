"""
QUESTION:
Write a function `update_array` that takes an array of integers as input and updates it by replacing all the zeroes with the nearest non-zero element. If the nearest non-zero element is on the left, use that; otherwise, use the nearest non-zero element on the right. If there are no non-zero elements on either side, replace the zero with the next larger non-zero element. If there are no larger non-zero elements, replace the zero with -1.
"""

def update_array(arr):
    n = len(arr)
    left = [-1] * n
    right = [-1] * n

    # Find the nearest non-zero element on the left side
    for i in range(1, n):
        if arr[i - 1] != 0:
            left[i] = arr[i - 1]

    # Find the nearest non-zero element on the right side
    for i in range(n - 2, -1, -1):
        if arr[i + 1] != 0:
            right[i] = arr[i + 1]

    # Update the array
    for i in range(n):
        if arr[i] == 0:
            if left[i] != -1:
                arr[i] = left[i]
            elif right[i] != -1:
                arr[i] = right[i]
            else:
                j = i + 1
                while j < n and arr[j] == 0:
                    j += 1
                if j < n:
                    arr[i] = arr[j]
                else:
                    arr[i] = -1

    return arr