"""
QUESTION:
You get a "text" and have to shift the vowels by "n" positions to the right.
(Negative value for n should shift to the left.)
"Position" means the vowel's position if taken as one item in a list of all vowels within the string.
A shift by 1 would mean, that every vowel shifts to the place of the next vowel.
Shifting over the edges of the text should continue at the other edge.

Example:

text = "This is a test!"
n = 1
output = "Thes is i tast!"

text = "This is a test!"
n = 3
output = "This as e tist!"

If text is null or empty return exactly this value.
Vowels are "a,e,i,o,u".



Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""

import re
from collections import deque

def shift_vowels(text, n):
    if not text:
        return text
    
    tokens = re.split('([aeiouAEIOU])', text)
    if len(tokens) > 1:
        vowels = deque(tokens[1::2])
        vowels.rotate(n)
        tokens[1::2] = vowels
    
    return ''.join(tokens)