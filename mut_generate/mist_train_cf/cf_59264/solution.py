"""
QUESTION:
Write a function `reverse_array` that takes an array of strings as input, reverses the order of its elements, and returns the reversed array. The function should not use existing reverse methods or libraries and should be case-insensitive, i.e., it should treat 'A' and 'a' as the same character.
"""

def reverse_array(arr):
    n = len(arr)
    output = [0] * n
    for i in range(n):
        output[n - i - 1] = arr[i].lower()
    return output