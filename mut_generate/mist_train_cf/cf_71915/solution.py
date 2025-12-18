"""
QUESTION:
Function: largeGroupPositions
Description: Given a string of lowercase letters, find all groups of 3 or more consecutive occurrences of the same character and return their start and end indices along with the frequency of the character in each group.
Restrictions: The input string has a length between 1 and 1000, inclusive, and contains only lowercase English letters. The output should be a list of tuples, where each tuple contains the interval of a large group and its frequency, sorted by the start index of the groups.
"""

def largeGroupPositions(s):
    result = []
    i = 0   # start index of each group

    for j in range(len(s)):
        if j == len(s) - 1 or s[j] != s[j+1]:   # end of group reached
            if j - i + 1 >= 3:   # check if group size is 3 or more
                result.append(([i, j], j - i + 1))   # append the group interval and frequency
            i = j + 1   # update start index of next group

    return result