"""
QUESTION:
Create a function `replace_palindrome_vowels` that takes a string as input, replaces every occurrence of 'a' with 'b', and returns the resulting string if it is a palindrome and contains exactly 3 vowels. If no such string can be found after 10 iterations, return "No valid string found".
"""

def replace_palindrome_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    replacement_count = 0
    
    while True:
        new_string = string.replace('a', 'b')
        
        if new_string == new_string[::-1] and new_string.count('a') + new_string.count('b') == 3:
            vowel_count = sum([new_string.count(vowel) for vowel in vowels])
            if vowel_count == 3:
                return new_string
        
        replacement_count += 1
        if replacement_count > 10:
            return "No valid string found"