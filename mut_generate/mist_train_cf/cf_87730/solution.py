"""
QUESTION:
Implement a recursive function called `find_most_frequent_char` that takes a string `s` as input and returns a tuple containing the most frequent character and its count. You cannot use built-in functions or libraries, and you must solve the problem without using any additional data structures.
"""

def find_most_frequent_char(s, max_char=None, max_count=0):
    if len(s) == 0:
        return max_char, max_count
    
    current_char = s[0]
    count = count_occurrences(s, current_char)
    
    if count > max_count:
        max_char = current_char
        max_count = count
    
    return find_most_frequent_char(s[1:], max_char, max_count)

def count_occurrences(s, char):
    if len(s) == 0:
        return 0
    
    if s[0] == char:
        return 1 + count_occurrences(s[1:], char)
    else:
        return count_occurrences(s[1:], char)