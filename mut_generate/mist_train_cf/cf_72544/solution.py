"""
QUESTION:
Create a recursive function called `recursive_multiply` that calculates the element-wise multiplication of two 1D arrays. The function should take two arrays as input, handle arrays of different sizes, and return the result of the multiplication. Implement the multiplication operation without using any built-in or third-party multiplication functions.
"""

def recursive_multiply(array1, array2, result=None, index=0):
    if result is None:
        result = []

    # Check if array sizes do not match
    if len(array1) != len(array2):
        return "Arrays do not match in size."

    # check if we reached the end of arrays
    elif index == len(array1):
        return result

    else:
        # append the product of the current indexed element to the result array
        result.append(array1[index] * array2[index])
        # Call the function recursively with the next index
        return recursive_multiply(array1, array2, result, index + 1)