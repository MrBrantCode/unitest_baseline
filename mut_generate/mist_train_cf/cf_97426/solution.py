"""
QUESTION:
Write a function `longest_substring(s)` that finds the length of the longest substring in a given string `s` that contains exactly three unique characters. The function should have a time complexity of O(n), where n is the length of the input string, and the input string can contain any printable ASCII characters.
"""

def longest_substring(s):
    # Initialize a dictionary to keep track of character frequencies
    freq = {}
    # Initialize two pointers: left and right
    left = right = 0
    # Initialize a variable to keep track of the maximum length
    max_length = 0

    # Iterate through the string using the right pointer
    while right < len(s):
        # If the current character is not in the dictionary, add it with a frequency of 1
        if s[right] not in freq:
            freq[s[right]] = 1
        # Otherwise, increment its frequency
        else:
            freq[s[right]] += 1

        # If the number of unique characters in the dictionary exceeds 3, move the left pointer and decrement the frequency of the character at the left pointer
        while len(freq) > 3:
            freq[s[left]] -= 1
            # If the frequency of the character at the left pointer becomes 0, remove it from the dictionary
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        # Update the maximum length if necessary
        max_length = max(max_length, right - left + 1)
        right += 1

    # Return the maximum length
    return max_length