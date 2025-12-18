"""
QUESTION:
Write a function `permutations` that generates all unique permutations of a given string. The function should be able to handle strings with duplicate characters and should have a time complexity of O(n * n!) and a space complexity of O(n!).
"""

def permutations(string):
    # Convert the string into a list of characters
    char_list = list(string)
    # Create a list to store all permutations
    result = []
    permute(char_list, 0, result)
    return result

def permute(char_list, start, result):
    # Base case: when start reaches the end of the string
    if start == len(char_list):
        # Convert the list of characters back into a string
        perm = ''.join(char_list)
        # Add the permutation to the result list
        result.append(perm)
    else:
        # Create a set to keep track of characters already used in the current position
        used = set()
        # Iterate through all possible characters to fill the current position
        for i in range(start, len(char_list)):
            # Check if the character has already been used
            if char_list[i] in used:
                continue
            # Swap the current character with the character at the start position
            char_list[start], char_list[i] = char_list[i], char_list[start]
            # Recursively generate permutations for the remaining characters
            permute(char_list, start + 1, result)
            # Swap back the characters to restore the original order
            char_list[start], char_list[i] = char_list[i], char_list[start]
            # Add the used character to the set
            used.add(char_list[i])