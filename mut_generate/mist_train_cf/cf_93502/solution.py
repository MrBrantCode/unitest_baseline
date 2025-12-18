"""
QUESTION:
Write a function called `find_permutations` that generates all possible permutations of a given string. The function should return a list of all unique permutations, and it should handle strings of any length. The time complexity of the solution should be O(n!), where n is the length of the input string.
"""

def find_permutations(string):
    # Helper function to find permutations recursively
    def backtrack(string, start, end, result):
        # Base case: if we have reached the end of the string
        if start == end:
            result.append("".join(string))
        else:
            for i in range(start, end + 1):
                # Swap characters
                string[start], string[i] = string[i], string[start]
                # Recursively find permutations of the remaining characters
                backtrack(string, start + 1, end, result)
                # Undo the swap
                string[start], string[i] = string[i], string[start]

    # Convert the string to a list of characters
    string = list(string)
    n = len(string)
    result = []
    # Find permutations recursively
    backtrack(string, 0, n - 1, result)
    # Return the list of permutations
    return result