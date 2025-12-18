"""
QUESTION:
Write
```python
word_pattern(pattern, string)
```
that given a ```pattern``` and a string ```str```, find if ```str``` follows the same sequence as ```pattern```. 

For example:
```python
word_pattern('abab', 'truck car truck car') == True
word_pattern('aaaa', 'dog dog dog dog') == True
word_pattern('abab', 'apple banana banana apple') == False
word_pattern('aaaa', 'cat cat dog cat') == False
```
"""

def word_pattern(pattern, string):
    x = list(pattern)
    y = string.split(' ')
    return len(x) == len(y) and len(set(x)) == len(set(y)) == len(set(zip(x, y)))