"""
QUESTION:
Given a nested array consisting of heterogeneous word elements, where each element can be either a string of alphanumeric characters or a nested array, write a function `find_max_length_word` that returns the string element with the maximum length located within the entire array structure. The nesting of arrays can go up to depth n. In case of multiple elements having the same maximum length, return any one of them. Assume all nested arrays are well-formed and are not circular.
"""

def find_max_length_word(nested_list):
    # Initialize max_length to 0 and max_word to empty string
    max_length = 0
    max_word = ""

    # Loop through elements in the nested list
    for element in nested_list:
        # If element is a string, check its length and update max_length and max_word if necessary
        if isinstance(element, str):
            if len(element) > max_length:
                max_length = len(element)
                max_word = element

        # If element is a list, recurse on the list and update max_length and max_word if necessary
        elif isinstance(element, list):
            word = find_max_length_word(element)
            if len(word) > max_length:
                max_length = len(word)
                max_word = word

    # Return the word with the maximum length
    return max_word