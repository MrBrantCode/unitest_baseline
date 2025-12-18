"""
QUESTION:
Write a function `correct_code(arr)` that takes a list of alphanumeric characters as input. The function should reverse the sequence of alphabetic characters in the list, while preserving the position of numeric characters. If the list contains no alphabetic characters, return the numerical array in its original order. The function should modify the input list in-place.
"""

def correct_code(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if not arr[left].isalpha():
            left += 1
            continue
        if arr[right].isdigit():
            right -= 1
            continue
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr