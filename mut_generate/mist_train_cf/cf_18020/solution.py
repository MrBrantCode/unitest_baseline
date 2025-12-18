"""
QUESTION:
Implement a function `get_permutations` that generates all possible permutations of a given string without using any built-in functions or libraries for generating permutations. The function should take a string as input and return a list of all possible permutations. The time complexity should be O(n!) and the space complexity should be O(n!), where n is the length of the input string.
"""

def get_permutations(string):
    # Helper function to swap characters at position i and j in the string
    def swap(string, i, j):
        char_list = list(string)
        char_list[i], char_list[j] = char_list[j], char_list[i]
        return ''.join(char_list)

    # Helper function to generate all permutations using backtracking
    def generate_permutations(string, start, end):
        if start == end:
            permutations.append(string)
        else:
            for i in range(start, end + 1):
                # Swap the current character with the first character
                # and generate permutations for the remaining characters
                string = swap(string, start, i)
                generate_permutations(string, start + 1, end)
                # Backtrack by swapping back the characters
                string = swap(string, start, i)

    permutations = []
    generate_permutations(string, 0, len(string) - 1)
    return permutations