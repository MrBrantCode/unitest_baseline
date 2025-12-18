"""
QUESTION:
Implement a function `permute(string, prefix)` that generates all permutations of a given string. The function should take two parameters: `string` and `prefix`, where `string` represents the remaining characters to be permuted and `prefix` represents the prefix of the current permutation. The function should not use any built-in permutation functions or libraries. The default value of `prefix` is an empty string.
"""

def permute(string, prefix=''):
    if len(string) == 0:
        print(prefix)
        return

    for i in range(len(string)):
        newString = string[:i] + string[i+1:]
        newPrefix = prefix + string[i]
        permute(newString, newPrefix)