"""
QUESTION:
Write a function `find_most_frequent` that takes a string `s` as input and returns the most frequently used alphanumeric character in the string. The function should be case insensitive and ignore punctuation and whitespace. The solution should use recursion.
"""

def find_most_frequent(s, i=0, d=None, max_char=None):
    s = s.lower()
    if not d:
        d = {}
        
    if i < len(s):
        if s[i].isalnum():
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if not max_char or d[s[i]] > d[max_char]:
                max_char = s[i]
        return find_most_frequent(s, i + 1, d, max_char)
    else:
        return max_char