"""
QUESTION:
Write a function `longest_palindrome(sentence)` that identifies the longest palindrome in a sentence while ignoring case sensitivity. The function should return the longest palindromic substring. Note that the input sentence can contain multiple words and the function should only consider alphanumeric characters as part of a palindrome, ignoring spaces and punctuation.
"""

def longest_palindrome(sentence):
    # Convert the sentence to lowercase and remove non-alphanumeric characters
    sentence = ''.join(char for char in sentence.lower() if char.isalnum())
    
    # Initialize variables to store the longest palindrome
    longest = ""
    length = 0
    
    # Loop through each substring of the sentence
    for i in range(len(sentence)):
        for j in range(i+1, len(sentence)+1):
            substring = sentence[i:j]
            # Check if the substring is a palindrome and longer than the current longest palindrome
            if substring == substring[::-1] and len(substring) > length:
                longest = substring
                length = len(substring)
    
    return longest