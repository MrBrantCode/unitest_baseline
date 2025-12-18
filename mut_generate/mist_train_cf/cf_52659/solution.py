"""
QUESTION:
Create a function `hyphenate_numbers` that takes a string `text` as input and returns the modified string with hyphens inserted between words that end with a number and start with an alphabet character, excluding instances within XML tags or email addresses.
"""

import re

def hyphenate_numbers(text):
    words = text.split()
    in_xml = False
    in_email = False
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        # check if we are in an XML tag
        if re.search('<[^>]*$', word):  # an opening tag without a closing tag
            in_xml = True
        elif re.search('>[^<]*$', word):  # a closing tag without an opening tag
            in_xml = False

        # check if we are in an email
        if re.search('\S+@\S+', word):  # an opening tag without a closing tag
            in_email = True
        elif in_email and word.endswith('>'):  # a closing tag without an opening tag
            in_email = False

        # if we are not in an XML tag or email and the current word ends with a number
        # and next word starts with alpha characters, insert a hyphen between them
        if not in_xml and not in_email and \
                re.search('\d$', word) and re.search('^[a-zA-Z]', next_word):
            words[i] = word + '-'

    return ' '.join(words)