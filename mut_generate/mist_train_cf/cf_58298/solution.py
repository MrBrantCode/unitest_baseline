"""
QUESTION:
Write a function `activate_order(arr)` that sorts a given list of strings `arr` according to the summation of ASCII values of each character of the string. In case of a tie, maintain the original order of appearance of the strings in the list.
"""

def activate_order(arr):
    # Summing ASCII values of each character in string using ord() function
    # Using enumerate to have the original index available in case of same ASCII sum
    sorted_arr = sorted(enumerate(arr), key=lambda x: (sum(ord(c) for c in x[1]), x[0]))
    # Extracting the string values from sorted_arr
    final_arr = [x[1] for x in sorted_arr]
    return final_arr