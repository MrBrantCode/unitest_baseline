"""
QUESTION:
Write a function `generate_permutations` that generates all possible permutations of a given string. The function should handle strings with duplicate characters, have a time complexity of O(n!), and return the permutations in lexicographically sorted order. The input is a string and the output is a list of strings.
"""

def generate_permutations(string):
    chars = list(string)
    result = []
    backtrack(chars, 0, result)
    result.sort()  
    return result

def backtrack(chars, start, result):
    if start == len(chars):
        result.append(''.join(chars))
        return

    used = set()

    for i in range(start, len(chars)):
        if chars[i] in used:
            continue
        used.add(chars[i])

        chars[start], chars[i] = chars[i], chars[start]

        backtrack(chars, start + 1, result)

        chars[start], chars[i] = chars[i], chars[start]