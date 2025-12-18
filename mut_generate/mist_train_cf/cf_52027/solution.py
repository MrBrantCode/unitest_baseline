"""
QUESTION:
Write a function named `swap_odd_even` that takes a string `input_str` as input and returns a string with every odd character swapped with the next even character, using no more than O(1) additional memory. The string is 0-indexed, and the first character is considered an odd character.
"""

def swap_odd_even(input_str):
    # Convert input string into a list
    str_list = list(input_str)

    # Traverse through the list with a step of 2 (reach each odd position)
    for i in range(0, len(str_list)-1, 2):
        # Swap the odd character with the next even character
        str_list[i], str_list[i+1] = str_list[i+1], str_list[i]

    # Convert list back to string and return
    return ''.join(str_list)