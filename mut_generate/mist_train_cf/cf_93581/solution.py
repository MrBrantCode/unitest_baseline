"""
QUESTION:
Write a function `are_anagrams` that determines if two input strings are anagrams of each other. The function should have a time complexity of O(n), where n is the length of the strings, and use constant space, without utilizing any built-in sorting or hashing functions. Assume the input strings only contain lowercase letters.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count1 = [0] * 26
    count2 = [0] * 26
    
    for i in range(len(str1)):
        count1[ord(str1[i]) - ord('a')] += 1
        count2[ord(str2[i]) - ord('a')] -= 1
    
    for i in range(26):
        if count1[i] != count2[i]:
            return False
    
    return True