"""
QUESTION:
Implement a function `reverse_string` that takes a string as input, reverses the order of its non-space characters (alphanumeric characters, special characters, and numbers), and returns the modified string. The function must preserve the original positions of the spaces in the string and ignore them during the reversal process.
"""

def reverse_string(str):
    # Convert the string to a list so that we can modify the characters in-place.
    list_str = list(str)
    i, j = 0, len(list_str) - 1
    while i < j:
        # Ignore spaces at the i-th position.
        if list_str[i] == " ":
            i += 1
            continue
        # Ignore spaces at the j-th position.
        if list_str[j] == " ":
            j -= 1
            continue
        # Swap the characters at the i-th and j-th positions.
        list_str[i], list_str[j] = list_str[j], list_str[i]
        i += 1
        j -= 1
    # Convert the list back to a string and return.
    return "".join(list_str)