"""
QUESTION:
Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned. 

```Python
format_words(['ninja', 'samurai', 'ronin']) # should return "ninja, samurai and ronin"
format_words(['ninja', '', 'ronin']) # should return "ninja and ronin"
format_words([]) # should return ""
```
```Haskell
formatWords ["ninja", "samurai", "ronin"] -- should return "ninja, samurai and ronin"
formatWords ["ninja", "", "ronin"] -- should return "ninja and ronin"
formatWords [] -- should return ""
```
"""

def format_words(words):
    if not words:
        return ''
    
    # Filter out empty strings
    filtered_words = [word for word in words if word]
    
    if not filtered_words:
        return ''
    
    if len(filtered_words) == 1:
        return filtered_words[0]
    
    # Join all but the last word with a comma, and add 'and' before the last word
    return ', '.join(filtered_words[:-1]) + ' and ' + filtered_words[-1]