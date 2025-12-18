"""
QUESTION:
Implement a function `binary_addition(array1, array2)` that takes two binary arrays as input, adds them together, and returns the result as a binary array. The function should handle carrying over values while adding, and it should not use any built-in functions featuring binary arithmetic or converting to integers for the addition process.
"""

def binary_addition(array1, array2):
    max_len = max(len(array1), len(array2))

    # Append zeros to the heads of both arrays until their lengths match
    array1 = ([0] * (max_len - len(array1))) + array1
    array2 = ([0] * (max_len - len(array2))) + array2

    result = [0] * max_len
    carry = 0

    # Iterate through the arrays from right to left
    for i in range(max_len - 1, -1, -1):
        temp = carry
        temp += 1 if array1[i] == 1 else 0
        temp += 1 if array2[i] == 1 else 0
        result[i] = 1 if temp % 2 == 1 else 0  
        carry = 0 if temp < 2 else 1  

    if carry != 0:
        result = [carry] + result

    return result