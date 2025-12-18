"""
QUESTION:
Write a function `replace_zeros` that takes an array of integers as input. Replace all zeros in the array with the product of neighboring non-zero elements. If a zero is at the start or end of the array, replace it with the non-zero neighbor. If there are multiple zeroes between non-zero numbers, replace them with the product of the surrounding non-zero numbers. If no neighbors exist, consider the product as 1.
"""

def replace_zeros(input_array):
    leftmost_nonzero = 1
    for i in range(len(input_array)):
        if input_array[i] == 0:
            j = i + 1
            while j < len(input_array) and input_array[j] == 0:
                j += 1
            rightmost_nonzero = input_array[j] if j < len(input_array) else 1
            for k in range(i, j):
                input_array[k] = leftmost_nonzero * rightmost_nonzero
            i = j - 1
        else:
            leftmost_nonzero = input_array[i]
    return input_array