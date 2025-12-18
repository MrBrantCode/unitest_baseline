"""
QUESTION:
Create a function named `reverse_join` that takes two string parameters `str1` and `str2`. The function should reverse both strings and then concatenate them. The resulting string should have the reversed `str1` followed by the reversed `str2`.
"""

def reverse_join(str1, str2):
    return str1[::-1] + str2[::-1]