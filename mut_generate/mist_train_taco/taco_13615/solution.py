"""
QUESTION:
### Description:

 Remove all exclamation marks from sentence except at the end.

### Examples

```
remove("Hi!") == "Hi!"
remove("Hi!!!") == "Hi!!!"
remove("!Hi") == "Hi"
remove("!Hi!") == "Hi!"
remove("Hi! Hi!") == "Hi Hi!"
remove("Hi") == "Hi"
```
"""

def remove_exclamation_marks(sentence: str) -> str:
    # Remove all exclamation marks from the sentence
    cleaned_sentence = sentence.replace('!', '')
    
    # Count the number of exclamation marks at the end of the original sentence
    trailing_exclamations = len(sentence) - len(sentence.rstrip('!'))
    
    # Append the same number of exclamation marks to the cleaned sentence
    result = cleaned_sentence + '!' * trailing_exclamations
    
    return result