"""
QUESTION:
Create a function called `longest_palindrome` that takes a string `s` as input and returns the longest palindrome within that string. The function should handle strings with both uppercase and lowercase letters, special characters, and spaces, and should be efficient for handling long and complex strings.
"""

def longest_palindrome(s):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s.lower()))
    # Initialize variables to keep track of the longest palindrome and its length
    longest_palindrome = ''
    max_length = 0
    # Loop through all possible substrings of the input string
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Update the longest palindrome and its length if necessary
                if len(substring) > max_length:
                    longest_palindrome = substring
                    max_length = len(substring)
    return longest_palindrome