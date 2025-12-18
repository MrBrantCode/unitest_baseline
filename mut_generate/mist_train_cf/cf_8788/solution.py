"""
QUESTION:
Write a function `find_unique_permutations` that takes a string `s` as input and prints all unique permutations of the string in lexicographic order. The function should not have any return value, but it should print each unique permutation on a separate line. The function should handle strings with duplicate characters and should not print duplicate permutations.
"""

def find_unique_permutations(s):
    # Convert the input string into a sorted list of characters
    chars = sorted(list(s))

    # Create an empty set to store the unique permutations
    unique_permutations = set()

    # Recursive function to generate all permutations
    def permute(current, remaining):
        # Base case: length of current permutation equals length of input string
        if len(current) == len(s):
            # Add current permutation to the set of unique permutations
            unique_permutations.add(''.join(current))
            return

        # Iterate through remaining characters
        for i in range(len(remaining)):
            # Append character to current permutation
            current.append(remaining[i])
            # Remove character from remaining characters
            new_remaining = remaining[:i] + remaining[i+1:]
            # Recursively call function with updated permutation and remaining characters
            permute(current, new_remaining)
            # Remove appended character for backtracking
            current.pop()

    # Call recursive function with initial permutation and all characters
    permute([], chars)

    # Convert set of unique permutations to list and sort lexicographically
    sorted_permutations = sorted(list(unique_permutations))

    # Print each permutation from the sorted list
    for permutation in sorted_permutations:
        print(permutation)