"""
QUESTION:
Design a data structure that supports the following two operations:

* `addWord` (or `add_word`) which adds a word,
* `search` which searches a literal word or a regular expression string containing lowercase letters `"a-z"` or `"."` where `"."` can represent any letter

You may assume that all given words contain only lowercase letters.

## Examples
```python
add_word("bad")
add_word("dad")
add_word("mad")

search("pad") == False
search("bad") == True
search(".ad") == True
search("b..") == True
```

**Note:** the data structure will be initialized multiple times during the tests!
"""

import re

def search_word_in_dictionary(words, search_word):
    """
    Searches for a word or regular expression in a dictionary of words.

    Parameters:
    - words (list): A list of words to be added to the dictionary.
    - search_word (str): The word or regular expression to search for.

    Returns:
    - bool: True if the search_word is found, False otherwise.
    """
    data = []
    
    # Add words to the data structure
    for word in words:
        data.append(word)
    
    # Search for the word
    for word in data:
        if re.match(search_word + '\\Z', word):
            return True
    return False