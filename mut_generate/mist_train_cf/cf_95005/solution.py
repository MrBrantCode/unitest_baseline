"""
QUESTION:
Write a function `get_permutations` that takes a string as input and returns a list of all possible permutations of that string. The function should not use any built-in functions or libraries for generating permutations. The time and space complexities of the function should be O(n!), where n is the length of the input string.
"""

def get_permutations(string):
    def swap(string, i, j):
        char_list = list(string)
        char_list[i], char_list[j] = char_list[j], char_list[i]
        return ''.join(char_list)

    def generate_permutations(string, start, end, permutations):
        if start == end:
            permutations.append(string)
        else:
            for i in range(start, end + 1):
                string = swap(string, start, i)
                generate_permutations(string, start + 1, end, permutations)
                string = swap(string, start, i)

    permutations = []
    generate_permutations(string, 0, len(string) - 1, permutations)
    return permutations