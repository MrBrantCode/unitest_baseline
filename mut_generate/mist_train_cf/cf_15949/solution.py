"""
QUESTION:
Implement a recursive function called `generate_combinations` that takes a string as input and returns all possible combinations of the input string. The function should not use any built-in combination functions and the input string is not empty.
"""

def generate_combinations(s):
    """
    Generate all possible combinations of the input string using backtracking.

    Args:
        s (str): The input string.

    Returns:
        list: A list of all possible combinations of the input string.
    """
    def backtrack(start, path):
        # if the current path has the same length as the input string,
        # it's a valid combination, so add it to the result list
        if len(path) == len(s):
            result.append("".join(path))
            return
        
        for i in range(len(s)):
            # skip the character if it's already in the current path
            if s[i] in path:
                continue
            # add the character to the current path
            path.append(s[i])
            # recursively call the backtrack function
            backtrack(start, path)
            # remove the last character from the current path
            path.pop()

    result = []
    backtrack(0, [])
    return result