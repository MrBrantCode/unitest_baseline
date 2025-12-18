"""
QUESTION:
Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right and "1", then the second letter from the left and the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

For example:
```python
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
"""

def char_concat(word):
    result = []
    length = len(word)
    
    # If the length is odd, drop the central element
    if length % 2 != 0:
        length -= 1
        mid_index = length // 2
        word = word[:mid_index] + word[mid_index + 1:]
    
    # Concatenate the characters as described
    for i in range(length // 2):
        result.append(word[i] + word[-(i + 1)] + str(i + 1))
    
    return ''.join(result)