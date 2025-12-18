"""
QUESTION:
Write a function named `unique_permutations` that generates all unique permutations of a given string without using any built-in functions or libraries for permutation generation. The function should optimize the permutation generation algorithm to minimize the number of recursive calls and reduce the time complexity. It should return a list of strings representing all unique permutations of the input string.

Note: The input string can contain duplicate characters.
"""

def unique_permutations(string):
    permutations = []
    permute(string, 0, len(string) - 1, permutations)
    return permutations

def permute(string, left, right, permutations):
    if left == right:
        permutations.append(string)
    else:
        for i in range(left, right + 1):
            if should_swap(string, left, i):
                string = swap(string, left, i)
                permute(string, left + 1, right, permutations)
                string = swap(string, left, i)  

def should_swap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return False
    return True

def swap(string, i, j):
    string_list = list(string)
    string_list[i], string_list[j] = string_list[j], string_list[i]
    return ''.join(string_list)