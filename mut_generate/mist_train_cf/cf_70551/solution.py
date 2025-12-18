"""
QUESTION:
Write a function named `string_manipulation` that takes a string `s` as input and performs the following operations: 

1. Remove leading and trailing spaces.
2. Replace each character in the string according to the given dictionary `dic`.
3. If a character appears consecutively, replace it with its corresponding value in `dic` only once.
4. Leave regular characters and special characters unaltered if they are not in `dic`.

The dictionary `dic` is given as `{'4': '61', 'b': '62', 'c': '63', 'd': '64', '3': '65', 'f': '6b', 'A': 'A1', '13': '42', 'C': '43', '0': '44', 'E': '45', 'T': '46', ' ': '%20'}`.
"""

def string_manipulation(s):
    dic = {'4': '61', 'b': '62', 'c': '63', 'd': '64', '3': '65', 'f': '6b', 
           'A': 'A1', '13': '42', 'C': '43', '0': '44', 'E': '45', 'T': '46', ' ': '%20'}

    if not s:
        return ""

    start = 0
    end = len(s) - 1

    while s[start] == ' ':
        start += 1
    while s[end] == ' ':
        end -= 1
    s = s[start:end+1]

    res = []
    i = 0

    while i < len(s):
        if s[i] in dic:
            while i + 1 < len(s) and s[i+1] == s[i]:
                i += 1
            res.append(dic[s[i]])
        else:
            res.append(s[i])
        i += 1

    return ''.join(res)