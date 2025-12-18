"""
QUESTION:
Write a function `count_extract_sort_number_strings_large(s)` that takes a string `s` as input, extracts all substrings containing numbers (both integers and floating point numbers), and returns two outputs: the count of these number-containing substrings and a list of these substrings in descending order of their numeric value. The function should be efficient enough to handle large strings and should ignore case and punctuation.
"""

import re

def count_extract_sort_number_strings_large(s):
    # finding all substrings that contain numbers.
    # \d captures digits, + means one or more, and .? to optionally capture a dot if 
    # it is followed by a digit.
    nums_strs = re.findall(r"(\d+\.?\d*)", s) 

    # converting each substring to float.
    nums_floats = [float(num) for num in nums_strs]

    # sorting and reversing to get descending order
    nums_floats.sort(reverse=True)
 
    # returning the count and the sorted list.
    return len(nums_strs), nums_floats 