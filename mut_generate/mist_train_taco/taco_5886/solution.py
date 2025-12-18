"""
QUESTION:
Find the second-to-last element of a list.

Example:
```python
penultimate([1,2,3,4])            # => 3
penultimate(["Python is dynamic"]) # => 'i'
(courtesy of [haskell.org](http://www.haskell.org/haskellwiki/99_questions/1_to_10))
```
"""

def find_penultimate(lst):
    return lst[-2]