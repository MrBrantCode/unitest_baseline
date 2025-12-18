"""
QUESTION:
Write a function `longest_word(string)` that takes a string of up to 1000 characters as input and returns the word with the longest length that contains at least two vowels and two consonants, with all vowels appearing before any consonants. The word is defined as a sequence of alphabetic characters separated by non-alphabetic characters.
"""

def longest_word(string):
    vowels = set('aeiou')
    longest = ""
    current = ""
    count_vowels = 0
    count_consonants = 0
    vowel_encountered_consonant = False
    
    for char in string:
        if char.isalpha():
            if char.lower() in vowels:
                if vowel_encountered_consonant:
                    current = char
                    count_vowels = 1
                    count_consonants = 0
                    vowel_encountered_consonant = False
                else:
                    count_vowels += 1
            else:
                if not vowel_encountered_consonant:
                    vowel_encountered_consonant = True
                count_consonants += 1
            current += char
            
            if count_vowels >= 2 and count_consonants >= 2:
                if len(current) > len(longest):
                    longest = current
        else:
            current = ""
            count_vowels = 0
            count_consonants = 0
            vowel_encountered_consonant = False
    
    return longest