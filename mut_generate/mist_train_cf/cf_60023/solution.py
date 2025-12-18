"""
QUESTION:
Write a function named `multiply` that takes two large integers as strings and returns their product as a string without using built-in multiplication. The function should handle large integers that exceed the standard data type's limit and should not convert the entire string to an integer for computation. The input strings are assumed to contain only valid digits.
"""

def multiply(num1, num2):
    res = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):  # iterating through num1 from end
        for j in reversed(range(len(num2))):  # iterating through num2 from end
            res[i + j + 1] += int(num1[i]) * int(num2[j]) # multiply current numbers and add to the position
            res[i + j] += res[i + j + 1] // 10  # carry over the number to left position
            res[i + j + 1] %= 10  # get the remaining value
    res = ''.join(map(str, res))  # convert the list of integers to string
    return res.lstrip('0') or '0'  # remove leading zeros and return '0' if result is zero