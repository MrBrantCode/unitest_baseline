"""
QUESTION:
Design a function `rearrange_array` that takes an array of integers as input and rearranges the array in-place such that all even elements appear before all odd elements. The function should return the rearranged array. The solution should not guarantee the relative order of the elements.
"""

def rearrange_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] % 2 == 0 and left < right:
            left += 1
        while arr[right] % 2 == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr