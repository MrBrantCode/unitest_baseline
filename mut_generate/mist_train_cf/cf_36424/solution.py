"""
QUESTION:
Write a function to determine the number of strings in a file that contain exactly two of the same letter and the number of strings that contain exactly three of the same letter. The file contains a list of strings, each representing a sequence of lowercase letters, one string per line.
"""

def count_letter_occurrences(s):
    two_count = 0
    three_count = 0
    letter_count = {}
    
    for line in s.split('\n'):
        line_count = {}
        for letter in line:
            if letter in line_count:
                line_count[letter] += 1
            else:
                line_count[letter] = 1
        if 2 in line_count.values():
            two_count += 1
        if 3 in line_count.values():
            three_count += 1
            
    return two_count, three_count