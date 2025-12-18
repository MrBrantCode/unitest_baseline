"""
QUESTION:
Create a function called `count_unique_three_letter_words` that takes a string of lowercase letters as input and returns the number of unique three-letter words (substrings of length 3) in the string. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_unique_three_letter_words(string):
    count = 0
    seen = [False] * (26*26*26)
    
    for i in range(len(string)-2):
        index = (ord(string[i]) - ord('a')) * 26*26 + (ord(string[i+1]) - ord('a')) * 26 + (ord(string[i+2]) - ord('a'))
        if not seen[index]:
            count += 1
            seen[index] = True
    
    return count