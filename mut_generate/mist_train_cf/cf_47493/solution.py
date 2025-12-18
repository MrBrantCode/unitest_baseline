"""
QUESTION:
Create a function named `str_combiner` that takes two non-empty string inputs, extracts the first three characters from each, and returns a new string that combines these characters. The function should operate in O(n) time complexity and include any special characters or spaces present in the initial three characters.
"""

def str_combiner(str1, str2):
    # get the first three ASCII characters of each string
    first_3_str1 = str1[:3]
    first_3_str2 = str2[:3]

    # concatenate and return the result
    return first_3_str1 + first_3_str2