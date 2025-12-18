"""
QUESTION:
Write a function `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all the strings in the list. The function should be case sensitive and consider only lowercase and uppercase letters. The function should have a time complexity of O(N*M), where N is the length of the list of strings and M is the average length of the strings, and use O(M) extra space. The input list can contain up to 10^6 strings, and the maximum length of each string is 10^4 characters.
"""

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the length of the shortest string
    min_length = min(len(string) for string in strings)

    # Iterate through the characters of the shortest string
    for i in range(min_length):
        # Check if all strings have the same character at the current position
        if not all(string[i] == strings[0][i] for string in strings):
            # Return the prefix up to the current position
            return strings[0][:i]

    # If all characters match, return the shortest string
    return strings[0][:min_length]