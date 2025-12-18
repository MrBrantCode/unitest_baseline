"""
QUESTION:
Design a function named `vowel_count` that takes a list of words as input and returns a tuple containing the total count of uppercase vowels and the highest occurring uppercase vowel. In the event of a tie, the function should return the vowel with the lower ASCII value.
"""

def vowel_count(words):
    vowel_freq = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

    for word in words:
        for character in word:
            if character in vowel_freq:
                vowel_freq[character] += 1
                
    max_freq = max(vowel_freq.values())
    total_vowels = sum(vowel_freq.values())
    
    for vowel in sorted(vowel_freq.keys()):
        if vowel_freq[vowel] == max_freq:
            highest_vowel = vowel
            break
            
    return total_vowels, highest_vowel