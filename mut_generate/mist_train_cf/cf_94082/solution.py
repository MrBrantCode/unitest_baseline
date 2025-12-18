"""
QUESTION:
Find the index of the first occurrence of a subsequence in a string. The subsequence consists of the digits of an integer in ascending order. 

Write a function `find_subsequence_index(string, integer)` that takes a string and an integer as input and returns the index of the first occurrence of the subsequence. Return -1 if the subsequence is not found. The function should have a time complexity of O(n), where n is the length of the string.
"""

def find_subsequence_index(string, integer):
    subsequence = ''.join(sorted(str(integer)))
    subsequence_index = 0
    for i in range(len(string)):
        if string[i] == subsequence[subsequence_index]:
            subsequence_index += 1
            if subsequence_index == len(subsequence):
                return i - subsequence_index + 1
    return -1