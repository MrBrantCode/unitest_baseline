"""
QUESTION:
Write a function `permute(string, prefix)` that generates all permutations of the input string without using any built-in permutation functions or libraries. The function should take two parameters: `string` and `prefix`, where `string` represents the remaining characters to be permuted and `prefix` represents the prefix of the current permutation. The function should not return anything but print each permutation. The `prefix` parameter is optional and defaults to an empty string.
"""

def permute(string, prefix=''):
    if len(string) == 0:
        print(prefix)
        return

    for i in range(len(string)):
        newString = string[:i] + string[i+1:]
        newPrefix = prefix + string[i]
        permute(newString, newPrefix)