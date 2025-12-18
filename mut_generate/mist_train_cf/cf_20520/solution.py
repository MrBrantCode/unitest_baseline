"""
QUESTION:
Create a function `character_frequency` that takes a string as input and returns a dictionary where each key is a letter or number from the string, and its corresponding value is the frequency of that character. The function should be case sensitive, exclude non-alphanumeric characters, and only include characters with a frequency of 2 or more. The dictionary should be sorted in descending order of frequency.
"""

def character_frequency(s):
    freq = {}
    for char in s:
        if char.isalnum():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    
    return {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True) if v >= 2}