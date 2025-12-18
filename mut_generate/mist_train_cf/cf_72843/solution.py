"""
QUESTION:
Implement a function `find_closest_vowel_subsequence(word)` that captures the nearest single sound-forming vowel or vowel pair nestled between two consonants within a word, starting the search from the word's terminal end. The function should be case-sensitive, ignore vowels at the onset or termination of the word, and only process words comprised of English alphabets. If the predefined conditions are not satisfied, the function should yield an empty string.
"""

def find_closest_vowel_subsequence(word):
    vowels = 'aeiouAEIOU'
    pairs = ['ea', 'ei', 'ie', 'ai', 'ay', 'ae', 'ei', 'ie', 'oy', 'au', 'eu', 'ui', 'uo', 'oa', 
             'oA', 'oi', 'oe', 'uA', 'io', 'eo', 'ia', 'ei']
    reversed_word = word[::-1]
    result = ""
    for i in range(1, len(reversed_word) - 1):
        if reversed_word[i] in vowels and reversed_word[i-1] not in vowels and reversed_word[i+1] not in vowels:
            result = reversed_word[i]
            break
        elif reversed_word[i:i+2][::-1].lower() in pairs and reversed_word[i-1] not in vowels and reversed_word[i+2] not in vowels:
            result = reversed_word[i:i+2][::-1]
            break
    return result