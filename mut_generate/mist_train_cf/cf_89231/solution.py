"""
QUESTION:
Implement a recursive function named `get_permutations(s)` that returns a list of all possible permutations of the characters in string `s`. All characters in `s` are unique. The function should have a time complexity of O(n * n!) and a space complexity of O(n!), where n is the length of the input string `s`.
"""

def get_permutations(s):
    # Base case: if the length of s is 1, return a list containing s
    if len(s) == 1:
        return [s]

    # Create an empty list to store the permutations
    permutations = []

    # Iterate over each character in s
    for i in range(len(s)):
        # Select the current character as the first character
        first_char = s[i]

        # Find all permutations of the remaining characters
        remaining_chars = s[:i] + s[i+1:]
        remaining_permutations = get_permutations(remaining_chars)

        # Combine the selected character with each permutation of the remaining characters
        for permutation in remaining_permutations:
            permutations.append(first_char + permutation)

    # Return the list of permutations
    return permutations