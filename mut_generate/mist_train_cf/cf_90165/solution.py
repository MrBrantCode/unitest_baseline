"""
QUESTION:
Generate a recursive function named `generate_permutations` that takes a string as input and returns a list of all possible permutations of the input string, including duplicate characters. The function should handle strings with duplicate characters and avoid generating duplicate permutations. The time complexity of the function should be O(n!), where n is the length of the input string.
"""

def generate_permutations(string):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(string) <= 1:
        return [string]

    # List to store permutations
    permutations = []

    # Set to keep track of already encountered characters
    encountered = set()

    # Recursive call to generate permutations
    for i in range(len(string)):
        # Check if the character has already been encountered
        if string[i] in encountered:
            continue

        # Add the character to the encountered set
        encountered.add(string[i])

        # Generate permutations for the remaining characters
        for perm in generate_permutations(string[:i] + string[i+1:]):
            permutations.append(string[i] + perm)

    return permutations