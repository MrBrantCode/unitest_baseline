"""
QUESTION:
Create a function called `count_occurrences(str1, str2)` that takes two string parameters and returns an integer representing the total number of non-overlapping occurrences of `str2` in `str1`, where each occurrence is surrounded by the character 'a'. The function should not count occurrences that overlap with each other or are not surrounded by 'a'.
"""

def count_occurrences(str1, str2):
    count = 0
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i+len(str2)] == str2 and (i == 0 or str1[i-1] == 'a') and (i+len(str2) == len(str1) or str1[i+len(str2)] == 'a'):
            count += 1
    return count