"""
QUESTION:
Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n).  The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.

example:
```javascript 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```ruby 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```python 
function sortIt('bid, zag', 2) #=> 'zag, bid'
```

The length of all words provided in the list will be >= n.  The format will be "x, x, x". In Haskell you'll get a list of `String`s instead.
"""

def sort_words_by_nth_char(words_string: str, n: int) -> str:
    # Split the input string into a list of words
    words = words_string.split(', ')
    
    # Sort the words based on the nth character (1-based index, so n-1 for 0-based index)
    sorted_words = sorted(words, key=lambda word: word[n - 1].lower())
    
    # Join the sorted words back into a string
    return ', '.join(sorted_words)