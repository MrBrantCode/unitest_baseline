"""
QUESTION:
Create a function `sort_strings(strings)` that takes a list of strings as input, sorts them in alphabetical order while ignoring the case of the letters, and returns the sorted list. The function should handle and preserve duplicate strings in the input list. The implementation must not use any built-in Python sorting functions or methods.
"""

def sort_strings(strings):
    # Convert all strings to lowercase for case-insensitive sorting
    lower_strings = [string.lower() for string in strings]

    # Create a list to store the sorted strings
    sorted_strings = []

    # Iterate through each string in the input list
    for string in strings:
        # Find the index where the string should be inserted in the sorted list
        index = 0
        for sorted_string in sorted_strings:
            # Compare the lowercase versions of the strings for case-insensitive sorting
            if lower_strings[strings.index(string)] > sorted_string.lower():
                index += 1
            else:
                break

        # Insert the string at the correct index in the sorted list
        sorted_strings.insert(index, string)

    return sorted_strings