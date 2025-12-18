"""
QUESTION:
Complete the solution so that it returns the number of times the search_text is found within the full_text.

```python
search_substr( fullText, searchText, allowOverlap = true )
```

so that overlapping solutions are (not) counted. If the searchText is empty, it should return `0`. Usage examples:

```python
search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', false ) # should return 1
```
"""

import re

def count_occurrences(full_text: str, search_text: str, allow_overlap: bool = True) -> int:
    if not search_text:
        return 0
    pattern = f'(?=({search_text}))' if allow_overlap else search_text
    return len(re.findall(pattern, full_text))