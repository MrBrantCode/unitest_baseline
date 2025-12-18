"""
QUESTION:
Implement a function named `check_strings_ends` that accepts an array of strings. The function should iterate over every string in the array and return a list of boolean values where each value represents whether the corresponding string ends with 'ing'. If a non-string value is encountered, include an error message in the output list instead of the boolean value. Handle unexpected errors and include the error message in the output list.
"""

def check_strings_ends(string_list):
    # Create an empty list to store the results
    result = []
    # For each item in the input list
    for string in string_list:
        try:
            # If the item is not a string, raise a ValueError
            if not isinstance(string, str):
               result.append("Error: Invalid input type, expected a string")
            # If the string ends with 'ing', append True to the result list
            elif string.endswith('ing'):
                result.append(True)
            # If the string does not end with 'ing', append False to the result list
            else:
                result.append(False)
        # If an unexpected error occurs, append the error message to the result list
        except Exception as e:
            result.append(str(e))
    # After all items in the input list have been processed, return the result list
    return result