"""
QUESTION:
Develop a function `find_least_common` that takes a string `text` as input and returns a tuple containing the word that appears the least amount of times and its frequency. The function should ignore case and consider 'Once' and 'once' as the same word. If there are multiple words with the same least frequency, the function can return any one of them.
"""

import re
from collections import Counter

def find_least_common(text):
    words = re.findall(r'\w+', text.lower()) 
    cnt = Counter(words)
    return min(cnt.items(), key=lambda x: x[1])