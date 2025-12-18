"""
QUESTION:
Our friendly friend Pete is really a nice person, but he tends to be rather... Inappropriate.

And possibly loud, if given enough ethanol and free rein, so we ask you to write a function that should take its not always "clean" speech and cover as much as possible of it, in order not to offend some more sensible spirits.

For example, given an input like
```
What the hell am I doing here? And where is my wallet? PETE SMASH!
```
You are expected to turn it into something like:
```
W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!
```
In case you didn't figure out the rules yet: any words longer than 2 characters need to have its "inside" (meaning every character which is not the first or the last) changed into `*`;  as we do not want Pete to scream too much, every uppercase letter which is not at the beginning of the string or coming after a punctuation mark among [".","!","?"] needs to be put to lowercase; spaces and other punctuation marks can be ignored.

Conversely, you need to be sure that the start of each sentence has a capitalized word at the beginning. Sentences are divided by the aforementioned punctuation marks.

Finally, the function will take an additional parameter consisting of an array/list of allowed words (upper or lower case) which are not to be replaced (the match has to be case insensitive).

Extra cookies if you can do it all in some efficient way and/or using our dear regexes ;)

**Note:** Absolutely not related to [a certain codewarrior I know](http://www.codewars.com/users/petegarvin1) :p
"""

import re

def clean_speech(speech, allowed_words=[]):
    PATTERN = re.compile(r'(?P<first>(?:(?<=[.!?] )|^)\w+)|(?P<other>\w+)')
    
    def transform_word(match):
        word = (match.group('first') or match.group('other')).lower()
        if word not in allowed_words and len(word) > 2:
            word = word[0] + '*' * (len(word) - 2) + word[-1]
        if match.group('first'):
            word = word.capitalize()
        return word
    
    allowed_words = set(map(str.lower, allowed_words))
    return PATTERN.sub(transform_word, speech)