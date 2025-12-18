"""
QUESTION:
Write a function `permute` that generates and returns all possible permutations of a given input string. The input string may contain duplicate characters. The function should take a string as input and return a list of strings, each representing a unique permutation of the input string.
"""

def permute(s):
    """
    Generates and returns all possible permutations of a given input string.
    
    Args:
    s (str): The input string.
    
    Returns:
    list: A list of strings, each representing a unique permutation of the input string.
    """
    def backtrack(sub_str, rest):
        if not rest:
            result.add(sub_str)
        else:
            for i in range(len(rest)):
                new_sub_str = sub_str + rest[i]
                new_rest = rest[:i] + rest[i+1:]
                backtrack(new_sub_str, new_rest)

    result = set()
    backtrack('', s)
    return list(result)