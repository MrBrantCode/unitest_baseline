"""
QUESTION:
You are given an array with several `"even"` words, one `"odd"` word, and some numbers mixed in.

Determine if any of the numbers in the array is the index of the `"odd"` word. If so, return `true`, otherwise `false`.
"""

def is_odd_word_index_in_array(arr):
    try:
        odd_index = arr.index('odd')
        return odd_index in arr
    except ValueError:
        # If 'odd' is not found in the array, return False
        return False