"""
QUESTION:
Create a function `find_substring` that takes two parameters, `string` and `substring`, and returns the number of occurrences of the `substring` in the `string` along with the positions (index) where the `substring` occurs. The function should have a time complexity of O(n), where n is the length of the `string`, and use a constant amount of additional space. The function should handle strings with a maximum length of 1 million characters, be case-sensitive, and consider the `substring` as a contiguous sequence of characters.
"""

def find_substring(string, substring):
    occurrences = 0
    positions = []

    len_string = len(string)
    len_substring = len(substring)

    if len_substring > len_string:
        return occurrences, positions

    for i in range(len_string - len_substring + 1):
        if string[i:i + len_substring] == substring:
            occurrences += 1
            positions.append(i)

    return occurrences, positions