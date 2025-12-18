"""
QUESTION:
Write a function `longest_palindrome(sentence)` that takes a string sentence as input and returns the longest palindrome substring in the sentence, ignoring case sensitivity. The function should only consider individual words in the sentence and their substrings as potential palindromes.
"""

def longest_palindrome(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Initialize variables to store the longest palindrome
    longest = ""
    length = 0
    
    # Loop through each word in the sentence
    for word in sentence.split():
        # Loop through each substring of the word
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substring = word[i:j]
                # Check if the substring is a palindrome and longer than the current longest palindrome
                if substring == substring[::-1] and len(substring) > length:
                    longest = substring
                    length = len(substring)
    
    return longest