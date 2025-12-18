"""
QUESTION:
Create a function `is_anagram(str1, str2)` that returns a boolean representing whether or not the input strings `str1` and `str2` are anagrams of each other. The function must have a time complexity of O(n^2), where n is the length of the strings, and a space complexity of O(n^2).
"""

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    def generate_permutations(string):
        if len(string) == 0:
            return ['']

        permutations = []
        for i in range(len(string)):
            substring = string[:i] + string[i+1:]
            for perm in generate_permutations(substring):
                permutations.append(string[i] + perm)

        return permutations

    perms = generate_permutations(str1)

    for perm in perms:
        if perm == str2:
            return True

    return False