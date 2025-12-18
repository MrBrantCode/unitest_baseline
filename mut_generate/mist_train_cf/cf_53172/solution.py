"""
QUESTION:
Implement a function named `find_substring_indexes` that takes two parameters: `substring` and `string`. The function should return a list of all starting indexes of `substring` in `string` without using built-in string search functions like `find()` or `index()`. The function should have a time complexity of O(N), where N is the length of the `string`.
"""

def find_substring_indexes(substring, string):
    indexes = []  # prepare an empty list to store the indices
    sub_len = len(substring)  # get the length of the substring
    for i in range(len(string)): # loop over the length of the string
        if string[i:i+sub_len] == substring:  # compare the substring with the part of string
            indexes.append(i)  # if a match is found, add the index to the list
    return indexes  # return the list of indices