"""
QUESTION:
Write a function `count_substring_occurrences(string, substring)` that takes two strings as input, and returns the number of occurrences of the substring in the string as separate words, ignoring any occurrences that are part of a larger word. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The comparison should be case-insensitive.
"""

def count_substring_occurrences(string, substring):
    # Initialize the count to 0
    count = 0

    # Convert the string and substring to lowercase
    string = string.lower()
    substring = substring.lower()

    # Split the string into words
    words = string.split()

    # Iterate through each word in the string
    for word in words:
        # If the word is the same as the substring, increment the count
        if word == substring:
            count += 1

    return count