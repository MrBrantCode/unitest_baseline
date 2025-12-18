"""
QUESTION:
Create a function named `anagram_count` that takes a string as input and returns the number of anagrams present in the string. The string may contain multiple words separated by spaces, punctuation, and varying cases. The function should ignore punctuation and be case-insensitive when considering anagrams.
"""

def anagram_count(s):
    s = s.lower()
    punctuation = "!@#$%^&*()_-+={}[]|\:;'<>,.?/"
    for char in punctuation:
        s = s.replace(char, "")

    words = s.split()
    groups = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []

        groups[sorted_word].append(word)
        
    count = 0
    for group in groups.values():
        if len(group) > 1:
            count += 1
            
    return count