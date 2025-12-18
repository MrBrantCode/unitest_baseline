"""
QUESTION:
Create a function `generate_array(n)` that takes a positive integer `n` as input and returns an array of integers from 0 to `n`. The array should exclude the number 3 and double the value of 5. The function should return an empty array if `n` is 0 or a negative number.
"""

def generate_array(n):
    result = []
    for i in range(n + 1):
        if i == 3:
            continue  # Skip number 3
        elif i == 5:
            result.append(2 * i)  # Double number 5
        else:
            result.append(i)
    return result