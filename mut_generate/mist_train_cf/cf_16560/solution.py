"""
QUESTION:
Create a function called `count_occurrences(str1, str2)` that takes in two string parameters and returns an integer representing the total number of non-overlapping occurrences of the second string (`str2`) in the first string (`str1`), where each occurrence is surrounded by the character 'a'.
"""

def count_occurrences(str1, str2):
    count = 0
    start = 0
    while start < len(str1):
        index = str1.find(str2, start)
        if index == -1:
            break
        if (index == 0 or str1[index-1] == 'a') and (index+len(str2) == len(str1) or str1[index+len(str2)] == 'a'):
            count += 1
            start = index + 1
        else:
            start = index + 1
    return count