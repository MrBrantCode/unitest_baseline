"""
QUESTION:
Create a function called `top_three_words` that takes a string of text as input and returns a list of the top three most frequently occurring words in the text, ignoring case sensitivity and punctuation. If the input text is empty or null, the function should return an error message.
"""

import collections
import re

def top_three_words(text):
    if text is None or text == '':
        return "The text is empty or null."

    text = text.lower() 
    words = re.findall(r'\b\w+\b', text)  
    words_counter = collections.Counter(words)   
    top_three = words_counter.most_common(3)   

    return [word for word, freq in top_three]