"""
QUESTION:
Write a function `generate_permutations(word)` that generates all unique permutations of the input string `word`. The function should not use any built-in library functions for generating permutations and should have a time complexity of O(n!). The function should also handle edge cases such as words with repeated letters or special characters, avoiding duplicate permutations.
"""

def generate_permutations(word):
    # Convert word to a list of characters
    chars = list(word)
    n = len(chars)
    permutations = []

    def backtrack(first):
        # If all characters have been used, add the permutation to the list
        if first == n:
            permutations.append(''.join(chars))

        for i in range(first, n):
            # Check if character at index i has already been used
            used = chars[first:i].count(chars[i])
            if used > 0:
                continue

            # Swap characters at indices first and i
            chars[first], chars[i] = chars[i], chars[first]

            # Generate permutations for the remaining characters
            backtrack(first + 1)

            # Swap back the characters
            chars[first], chars[i] = chars[i], chars[first]

    # Call the backtrack function with the initial index 0
    backtrack(0)

    return permutations