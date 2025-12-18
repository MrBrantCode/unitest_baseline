"""
QUESTION:
Write a function `reverse_alphabets_in_words` that takes a string of text as input and returns a new string where the alphabetic characters in each individual word are reversed, while maintaining the original word and sentence order, and preserving non-alphabetic characters in their original positions.
"""

def reverse_alphabets_in_words(text):
    # Split the string into words
    words = text.split(' ')
    
    reversed_words = []
    
    # Reverse the alphabetic characters in each word
    for word in words:
        chars = list(word)
        l, r = 0, len(chars) - 1
        while l < r:
            if not chars[l].isalpha():
                l += 1
            elif not chars[r].isalpha():
                r -= 1
            else:
                # Swap letters at positions "l" and "r"
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        reversed_words.append(''.join(chars))
        
    # Join the words back together into a sentence and return
    return ' '.join(reversed_words)