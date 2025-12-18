"""
QUESTION:
Create a function 'subStr' that takes a string and two indices as input, a start index and an end index. The function should return a substring between the start and end index, inclusive of the start index and exclusive of the end index. The function should handle edge cases such as when the start index is greater than the end index, when the start index is less than 0, and when the end index is greater than the length of the string. The time complexity of the function should be O(n), where n is the length of the string.
"""

def subStr(string, start, end):
    if start >= end or start < 0 or start >= len(string) or end > len(string):
        return ""

    substring = ""
    for i in range(start, end):
        substring += string[i]

    return substring