"""
QUESTION:
You're a programmer in a SEO company. The SEO specialist of your company gets the list of all project keywords everyday, then he looks for the longest keys to analyze them.

You will get the list with keywords and must write a simple function that returns the biggest search keywords and sorts them in lexicographical order.

For instance you might get:
```python
'key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1'
```

And your function should return:
```python
"'bigkey1', 'bigkey2'"
```

Don't forget to rate this kata! Thanks :)
"""

def find_longest_keywords(*keywords):
    # Sort the keywords by length in descending order, and by lexicographical order for ties
    sorted_keywords = sorted(keywords, key=lambda key: (-len(key), key))
    
    # Find the index where the length of the keywords changes
    i = next((i for i, key in enumerate(sorted_keywords) if len(key) != len(sorted_keywords[0])), None)
    
    # Extract the longest keywords
    longest_keywords = sorted_keywords[:i] if i is not None else sorted_keywords
    
    # Return the longest keywords as a formatted string
    return str(longest_keywords)[1:-1] or "''"