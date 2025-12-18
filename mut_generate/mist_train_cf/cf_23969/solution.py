"""
QUESTION:
Create a function `generate_strings(set, k)` that generates all possible strings of length `k` from a given set of lowercase characters. The function should take two parameters: `set`, a set of lowercase characters, and `k`, the desired length of the strings.
"""

def generate_strings(char_set, length):
    strings = []
    n = len(char_set)

    def generate_strings_recur(sub, count):
        if count == 0:
            strings.append(sub)
            return
        
        for i in range(n):
            new_sub = sub + char_set[i]
            generate_strings_recur(new_sub, count-1)

    count = length
    sub = ""
    generate_strings_recur(sub, count)
    return strings