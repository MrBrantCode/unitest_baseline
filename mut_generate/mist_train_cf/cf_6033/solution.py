"""
QUESTION:
Implement a recursive function get_permutations(s) that returns a list of all possible permutations of the characters in string s, where all characters in s are unique. The function should have a time complexity of O(n * n!) and a space complexity of O(n!), where n is the length of the input string s.
"""

def get_permutations(s):
    if len(s) == 1:
        return [s]

    permutations = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        remaining_permutations = get_permutations(remaining_chars)
        for permutation in remaining_permutations:
            permutations.append(first_char + permutation)
    return permutations