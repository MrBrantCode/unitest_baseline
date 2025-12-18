"""
QUESTION:
Create a function `unique_words_with_vowels` that takes a string as input and returns a list of unique words in alphabetical order. The returned list should include only words that do not start with a vowel and contain at least one vowel, but do not contain a consecutive string of three or more vowels. The function should be case-sensitive. The time complexity of the function should be O(n), where n is the length of the input string, and the space complexity should be O(m), where m is the number of unique words that meet the given criteria.
"""

def unique_words_with_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_set = set()
    
    words = string.split()
    
    for word in words:
        # Check if word starts with a vowel
        if word[0].lower() in vowels:
            continue
        
        # Check if word contains consecutive string of three or more vowels
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
        
        # Check if word contains at least one vowel
        has_vowels = any(letter.lower() in vowels for letter in word)
        if has_vowels:
            word_set.add(word)
    
    return sorted(list(word_set))