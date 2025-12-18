"""
QUESTION:
Create a function `sieve_repeating_elements(input_list)` that takes a list of strings as input, removes leading and trailing spaces, and ignores case sensitivity. The function should return a list of strings that appear more than once in the input list, considering numeric strings as well. The output list should not contain any duplicates.
"""

def sieve_repeating_elements(input_list):
    # Clean the items (strip, case sensitive)
    cleaned_list = [item.strip().lower() for item in input_list]

    # Initialize output
    output_list = []

    # Loop to add repeated strings to output
    for item in cleaned_list:
        if cleaned_list.count(item) > 1 and item not in output_list:
            output_list.append(item)
            cleaned_list = [i for i in cleaned_list if i != item]
    return output_list