"""
QUESTION:
Create a function named `reverse_alphabetical_order` that takes a string `s` as input, removes all whitespace characters, applies the QuickSort algorithm to sort the remaining characters in reverse alphabetical order, and returns the rearranged string.
"""

def reverse_alphabetical_order(s):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        return quick_sort(left) + middle + quick_sort(right)

    # Remove whitespaces and sort
    rearranged_string = quick_sort([char for char in s if char != ' ']) 
    return ''.join(rearranged_string)