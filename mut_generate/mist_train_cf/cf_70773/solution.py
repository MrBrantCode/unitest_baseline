"""
QUESTION:
Create a function `swap_odd_even_characters` that takes an input string. The function should swap every odd character in the input string with the next even character, leaving all other characters unchanged. Note that indexing is zero-based, meaning the first character is at index 0, so odd characters are at even indices and even characters are at odd indices. If the length of the string is odd, the last character should be left unchanged. The function should return the modified string.
"""

def swap_odd_even_characters(input_string):
    list_string = list(input_string)
    for i in range(0, len(list_string) - 1, 2):
        list_string[i], list_string[i+1] = list_string[i+1], list_string[i]
    output_string = ''.join(list_string)
    return output_string