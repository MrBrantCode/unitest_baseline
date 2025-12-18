"""
QUESTION:
Write a function called `generate_permutations` that takes a string as input and returns all possible permutations of the string. The function should only consider strings with a maximum length of 15 characters. If the string is empty or contains only one character, the function should return a list containing the string itself. Otherwise, it should recursively generate permutations by iterating over each character in the string, removing it, and appending it to each permutation of the remaining characters.
"""

def generate_permutations(string):
    if len(string) > 15:
        return []
    
    permutations = []
    if len(string) <= 1:
        permutations.append(string)
    else:
        for i in range(len(string)):
            first = string[i]
            remaining = string[:i] + string[i+1:]
            for sub_permutation in generate_permutations(remaining):
                permutations.append(first + sub_permutation)
    return permutations