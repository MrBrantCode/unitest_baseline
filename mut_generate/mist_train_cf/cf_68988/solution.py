"""
QUESTION:
Write a function called `max_consonant_word` that accepts a dictionary with English words as keys and their French translations as values. The function should return the key with the maximum quantity of consonant letters. In case of a tie, return the key with consonants having the highest total ASCII value. The function should be case-insensitive and should ignore non-word or non-English keys/values.
"""

def max_consonant_word(dict_english_french):
    import re
    
    def get_words(word):
        if isinstance(word, str) and bool(re.fullmatch('^[a-zA-Z\s]*$', word)):
            return word
        else:
            return False
            
    def ascii_sum(word):
        return sum(ord(i) for i in word.lower() if i in "bcdfghjklmnpqrstvwxyz")
    
    def consonant_count(word):
        return len([i for i in word.lower() if i in "bcdfghjklmnpqrstvwxyz"])
    
    max_consonant_keyword = ''
    max_consonants = 0
    max_ascii = 0
    
    for keyword in dict_english_french.keys():
        word = get_words(keyword)
        if word:
            consonant_c = consonant_count(word)
            if consonant_c > max_consonants or \
            (consonant_c == max_consonants and ascii_sum(word) > max_ascii):
                max_consonants = consonant_c
                max_consonant_keyword = keyword
                max_ascii = ascii_sum(word)
                
    return max_consonant_keyword