"""
QUESTION:
Write a function `len_text(array, k)` that takes an array of strings and an integer `k` as parameters. Each string in the array contains a mix of alphanumeric and special characters. Return the longest string from the array where the count of alphanumeric characters does not exceed `k`.
"""

def len_text(array, k):
    max_len = 0
    lengthy_text = ''
    for i in array:
        count = sum(c.isalnum() for c in i)
        if count > max_len and count <= k:
            max_len = count
            lengthy_text = i
    return lengthy_text