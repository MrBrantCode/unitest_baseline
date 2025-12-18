"""
QUESTION:
Create a function named `sort_and_convert` that takes a list of strings as input. The function should remove any duplicate strings from the list, then sort the remaining strings in descending order of their lengths. The function should treat non-string elements as strings. Finally, convert the sorted list to all uppercase letters. The solution must have a time complexity of O(n^2) and cannot use built-in sorting or duplicate removal functions.
"""

def sort_and_convert(strings):
    """
    Removes duplicates from a list of strings, sorts them in descending order of their lengths,
    and converts them to all uppercase letters.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of unique strings in descending order of their lengths, all in uppercase.
    """
    # Remove duplicates
    unique_strings = []
    for string in strings:
        if str(string) not in unique_strings:
            unique_strings.append(str(string))
    
    # Sort by reverse order of length
    for i in range(len(unique_strings)):
        for j in range(i + 1, len(unique_strings)):
            if len(unique_strings[i]) < len(unique_strings[j]):
                unique_strings[i], unique_strings[j] = unique_strings[j], unique_strings[i]
    
    # Convert to uppercase
    return [string.upper() for string in unique_strings]