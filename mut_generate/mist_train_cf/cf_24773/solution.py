"""
QUESTION:
Write a function `same_frequency(num1, num2)` that determines whether two given numbers have the same frequency of digits. The function should return `True` if the frequency of digits in `num1` and `num2` is the same, and `False` otherwise. The function should assume that both inputs are non-negative integers.
"""

def same_frequency(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    if len(str1) != len(str2):
        return False
    dict = {}
    for char in str1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in str2:
        if not char in dict:
            return False
        dict[char] -= 1
    for k in dict:
        if dict[k] != 0:
            return False
    return True