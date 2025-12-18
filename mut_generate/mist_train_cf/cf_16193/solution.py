"""
QUESTION:
Implement a function named `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all strings in the list. The function should consider case sensitivity and handle any character encoding, including Unicode. The input list can contain up to 10^6 strings, and the maximum length of each string is 10^4 characters. The function should have a time complexity of O(N*M), where N is the length of the list of strings and M is the average length of the strings, and use O(M) extra space.
"""

def entrance(strings):
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