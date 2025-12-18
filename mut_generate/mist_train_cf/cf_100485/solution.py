"""
QUESTION:
Create a function named `palindrome_names` that takes a list of names as input and returns a new list containing only the names that are spelled the same way forward and backward (palindromes). The function should ignore case and spaces in the names. Do not use Python's built-in palindrome function.
"""

def palindrome_names(names):
    palindrome_list = []
    for name in names:
        # Remove any spaces and convert to lowercase
        name = name.replace(" ", "").lower()
        # Check if the name is equal to its reverse
        if name == name[::-1]:
            palindrome_list.append(name)
    return palindrome_list