"""
QUESTION:
Create a function named `unique_words_with_vowels` that takes a string as input and returns a list of unique words that contain at least one vowel, but do not start with a vowel and do not contain a consecutive string of three or more vowels. The function should be case-sensitive and the returned list should be sorted in alphabetical order. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(m), where m is the number of unique words that meet the given criteria.
"""

def unique_words_with_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_set = set()
    
    words = string.split()
    
    for word in words:
        if word[0].lower() in vowels:
            continue
        
        has_consecutive_vowels = False
        count = 0
        for letter in word:
            if letter.lower() in vowels:
                count += 1
                if count >= 3:
                    has_consecutive_vowels = True
                    break
            else:
                count = 0
        
        if has_consecutive_vowels:
            continue
        
        if any(letter.lower() in vowels for letter in word):
            word_set.add(word)
    
    return sorted(list(word_set))