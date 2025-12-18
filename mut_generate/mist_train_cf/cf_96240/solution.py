"""
QUESTION:
Implement a function `count_substring_ab(string, index, count)` to find the number of times the substring "ab" appears in the given string, considering both uppercase and lowercase letters, with a time complexity of O(n), where n is the length of the input string. The input string will have a maximum length of 1000 characters and will only contain alphabets.
"""

def count_substring_ab(string, index, count):
    if index >= len(string):
        return count

    if string[index:index+2].lower() == "ab":
        count += 1

    return count_substring_ab(string, index + 1, count)