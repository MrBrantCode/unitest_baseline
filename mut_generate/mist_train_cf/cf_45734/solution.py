"""
QUESTION:
Define a function `find_frequent` that accepts a list of strings containing alphanumeric characters. The function should return the alphanumeric character that appears the most frequently across all strings, ignoring case. If multiple characters have the same frequency, return the one that appears first in the concatenated strings.
"""

def find_frequent(strings):
    from collections import Counter 
    c = Counter()
    
    for string in strings:
        string = string.lower()
        for char in string:
            if char.isalnum():
                c[char] += 1

    most_frequent = c.most_common(1)
    
    # In case if there are multiple values with maximum count, take the first from the strings
    if len(most_frequent)>0 and most_frequent[0][1] > 1:
        max_count = most_frequent[0][1]
        most_frequent_chars = [i for i in c if c[i] == max_count]
        for char in "".join(strings).lower():
            if char in most_frequent_chars:
                return char
    
    return None