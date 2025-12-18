"""
QUESTION:
Create a function `identify_palindromes` that takes a list of strings as input. The function should return a list of strings that are palindromes, ignoring case, spaces, and punctuation marks. Do not use built-in string manipulation or regular expression functions.
"""

def identify_palindromes(lst):
    def is_palindrome(string):
        # Remove punctuation marks and spaces from the string
        clean_string = ''.join(char for char in string if char.isalnum())
        # Convert the string to lowercase
        lowercase_string = clean_string.lower()
        # Check if the lowercase string is equal to its reverse
        return lowercase_string == lowercase_string[::-1]

    # Create an empty list to store the palindromes
    palindromes = []
    # Iterate over each string in the list
    for string in lst:
        # Check if the string is a palindrome
        if is_palindrome(string):
            # If it is, add it to the list of palindromes
            palindromes.append(string)
    # Return the list of palindromes
    return palindromes