"""
QUESTION:
Implement a function named `compare_strings` that takes two strings of lowercase letters as input and returns an integer value representing their alphabetical order. The function must implement its own sorting algorithm to sort the characters within each string and compare the sorted strings based on their ASCII values. The output should be -1 if the first string comes before the second string, 1 if the second string comes before the first string, and 0 if both strings are the same.
"""

def sort_string(s):
    chars = list(s)
    for i in range(len(chars)):
        for j in range(len(chars) - 1 - i):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)

def compare_strings(s1, s2):
    sorted_s1 = sort_string(s1)
    sorted_s2 = sort_string(s2)
    for i in range(len(sorted_s1)):
        if sorted_s1[i] < sorted_s2[i]:
            return -1
        elif sorted_s1[i] > sorted_s2[i]:
            return 1
    return 0