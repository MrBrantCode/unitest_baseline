"""
QUESTION:
Write a function `longest_substring` that takes a string `s` and an integer `k` as input and returns the length of the longest substring of `s` that contains exactly `k` unique characters. The function should have a time complexity of O(n), where n is the length of `s`.
"""

def longest_substring(s, k):
    # Initialize a dictionary to keep track of the count of each character
    count = {}

    # Initialize pointers for the start and end of the substring
    start = 0
    end = 0

    # Initialize variables to keep track of the maximum length and unique characters
    max_length = 0
    unique_chars = 0

    # Iterate through the string
    while end < len(s):
        # Add the current character to the count dictionary
        count[s[end]] = count.get(s[end], 0) + 1

        # If the count of the current character is 1, increment unique_chars
        if count[s[end]] == 1:
            unique_chars += 1

        # If unique_chars is greater than k, move the start pointer and update the count dictionary
        while unique_chars > k:
            count[s[start]] -= 1
            if count[s[start]] == 0:
                unique_chars -= 1
            start += 1

        # Update the maximum length if necessary
        max_length = max(max_length, end - start + 1)

        # Move the end pointer to the next character
        end += 1

    # Return the maximum length
    return max_length