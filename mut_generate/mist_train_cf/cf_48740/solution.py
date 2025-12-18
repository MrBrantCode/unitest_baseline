"""
QUESTION:
Implement the function `reverse_arr(input_arr)` to reverse the order of an array of integers without using any predefined or built-in methods. The function should handle edge cases, such as empty arrays or arrays of length 1, and should be efficient in terms of time and space complexity.
"""

def reverse_arr(input_arr):
    left = 0
    right = len(input_arr) - 1
    while left < right:
        input_arr[left], input_arr[right] = input_arr[right], input_arr[left]  
        left += 1
        right -= 1
    return input_arr