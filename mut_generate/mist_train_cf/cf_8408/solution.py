"""
QUESTION:
Write a function named `generate_permutations(s)` that generates all unique permutations of a given string `s` in lexicographically sorted order. The function should handle strings containing duplicate characters and special characters correctly. The time complexity should be O(n!), where n is the length of the string, and the space complexity should be optimized to avoid unnecessary memory usage.
"""

from collections import Counter

def generate_permutations(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Convert the Counter object to a list of tuples
    char_freq = list(char_count.items())

    # Sort the list of tuples lexicographically
    char_freq.sort()

    # Create a list to store the permutations
    permutations = []

    # Generate permutations using backtracking
    def backtrack(char_freq, curr_perm, permutations, n):
        # Base case: if the current permutation has the same length as the original string
        if len(curr_perm) == n:
            # Convert the list of characters to a string and append it to the permutations list
            permutations.append(''.join(curr_perm))
            return

        # Iterate through the character-frequency pairs
        for i in range(len(char_freq)):
            # Get the current character and its frequency
            char, freq = char_freq[i]

            # If the frequency is 0, skip this character
            if freq == 0:
                continue

            # Add the current character to the current permutation
            curr_perm.append(char)

            # Decrement the frequency of the current character
            char_freq[i] = (char, freq - 1)

            # Recursively generate permutations with the updated character-frequency pairs
            backtrack(char_freq, curr_perm, permutations, n)

            # Remove the current character from the current permutation
            curr_perm.pop()

            # Increment the frequency of the current character
            char_freq[i] = (char, freq)

    backtrack(char_freq, [], permutations, len(s))
    return permutations