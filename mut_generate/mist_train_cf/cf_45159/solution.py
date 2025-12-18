"""
QUESTION:
Design a function named `hyphenate_numbers` that takes a string as input and returns a string where hyphens are inserted in the spaces separating words that end with numerical digits. The function should handle multiple numerical formats, ignore numbers within parentheses or quotes, and preserve non-Latin scripts, emojis, XML tags, and email addresses without modifying the spaces within them.
"""

import re

def hyphenate_numbers(text):
    words = text.split()
    in_xml = False
    in_email = False
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i+1]
        
        # check if we are in an XML tag
        if re.search('<[^>]*$', word):  
            in_xml = True
        elif re.search('>[^<]*$', word):  
            in_xml = False
            
        # check if we are in an email
        if re.search('\S+@\S+', word):  
            in_email = True
        elif in_email and word.endswith('>'):  
            in_email = False
        
        # if we are not in an XML tag or email and the current word ends with a number
        # and next word starts with alpha characters, insert a hyphen between them
        if not in_xml and not in_email and \
           re.search('\d$', word) and re.search('^[a-zA-Z]', next_word):
            words[i] = word + '-'

    return ' '.join(words)