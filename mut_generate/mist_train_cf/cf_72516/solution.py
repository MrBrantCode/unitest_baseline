"""
QUESTION:
Create a function `are_palindrome_anagrams(s1, s2)` that takes two alphanumeric sequences `s1` and `s2` as input and returns a boolean value indicating whether they are palindrome anagrams of each other. The function should ignore non-alphanumeric characters and be case-insensitive.
"""

def are_palindrome_anagrams(s1, s2):
    # Remove any character that's not alphanumeric and convert to lower case
    s1 = ''.join(ch for ch in s1 if ch.isalnum()).lower()
    s2 = ''.join(ch for ch in s2 if ch.isalnum()).lower()

    # To be palindrome anagrams, they need to be the same length
    if len(s1) != len(s2):
        return False

    # Create dictionaries to count character occurrences
    count1 = {}
    count2 = {}
    
    for ch in s1:
        if ch in count1:
            count1[ch] += 1
        else:
            count1[ch] = 1
            
    for ch in s2:
        if ch in count2:
            count2[ch] += 1
        else:
            count2[ch] = 1
    
    # If the histograms are the same, they are palindrome anagrams
    return count1 == count2