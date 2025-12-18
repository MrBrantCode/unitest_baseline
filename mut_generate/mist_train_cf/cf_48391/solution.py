"""
QUESTION:
Create a function `checkPalindromeAnagram(sequence)` that determines if a given sequence of characters can be rearranged into a palindrome. The function should return `True` if the sequence can be rearranged into a palindrome and `False` otherwise. The input sequence will consist of ASCII characters and the function should be case sensitive, treating uppercase and lowercase characters as distinct.
"""

def checkPalindromeAnagram(sequence):
    characterCounts = [0]*128
    for char in sequence:
        characterCounts[ord(char)] += 1
    
    oddCount = 0
    for count in characterCounts:
        oddCount += count % 2
    
    return oddCount <= 1