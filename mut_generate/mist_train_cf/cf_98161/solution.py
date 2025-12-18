"""
QUESTION:
Create a function `palindrome_names(names)` that takes a list of names as input and returns a new list containing only the names that are spelled the same way forward and backward (palindromes), without using Python's built-in palindrome function. The function should ignore case and spaces when checking for palindromes.
"""

def palindrome_names(names):
    palindrome_list = []
    for name in names:
        name = name.replace(" ", "").lower()
        if name == name[::-1]:
            palindrome_list.append(name)
    return palindrome_list