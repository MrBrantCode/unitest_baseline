"""
QUESTION:
Implement a function which 
creates a **[radix tree](https://en.wikipedia.org/wiki/Radix_tree)** (a space-optimized trie [prefix tree]) 
in which each node that is the only child is merged with its parent [unless a word from the input ends there]) 
from a given list of words 
using dictionaries (aka hash maps or hash tables) where:

1. The dictionary keys are the nodes.
2. Leaf nodes are empty dictionaries.
3. The value for empty input is an empty dictionary.
4. Words are all lowercase or empty strings.
5. Words can contain duplicates.

### Examples:

```python
>>> radix_tree()
{}

>>> radix_tree("")
{}

>>> radix_tree("", "")
{}

>>> radix_tree("radix", "tree")
{"radix": {}, "tree": {}}

>>> radix_tree("ape", "apple")
{"ap": {"e": {}, "ple": {}}}

>>> radix_tree("apple", "applet", "apple", "ape")
{"ap": {"ple": {"t": {}}, "e": {}}}

>>> radix_tree("romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus")
{"r": {"om": {"an": {"e": {}, "us": {}}, "ulus": {}},
       "ub": {"ens": {}, "ic": {"on": {}, "undus": {}}}}}

>>> radix_tree("appleabcd", "apple")
{"apple": {"abcd": {}}}
```
"""

from itertools import groupby
from operator import itemgetter
from os.path import commonprefix

def build_radix_tree(*words):
    # Filter out empty words
    words = [w for w in words if w]
    
    # Base case: if no words, return an empty dictionary
    if not words:
        return {}
    
    # Initialize the result dictionary
    result = {}
    
    # Group words by their first character
    for key, grp in groupby(sorted(words), key=itemgetter(0)):
        lst = list(grp)
        prefix = commonprefix(lst)
        # Recursively build the subtree for the remaining part of the words
        result[prefix] = build_radix_tree(*(w[len(prefix):] for w in lst))
    
    return result