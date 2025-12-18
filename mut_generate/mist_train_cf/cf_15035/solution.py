"""
QUESTION:
Write a function `find_permutations` that takes a string as input and returns a list of all its permutations. The function should have a time complexity of O(n!), where n is the length of the input string.
"""

def find_permutations(string):
    def backtrack(string, start, end, result):
        if start == end:
            result.append("".join(string))
        else:
            for i in range(start, end + 1):
                string[start], string[i] = string[i], string[start]
                backtrack(string, start + 1, end, result)
                string[start], string[i] = string[i], string[start]

    string = list(string)
    n = len(string)
    result = []
    backtrack(string, 0, n - 1, result)
    return result