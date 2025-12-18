"""
QUESTION:
Given any number of boolean flags function should return true if and only if one of them is true while others are false. If function is called without arguments it should return false.

```python
  only_one() == False
  only_one(True, False, False) == True
  only_one(True, False, False, True) == False
  only_one(False, False, False, False) == False  
```
"""

def exactly_one_true(*args):
    return sum(args) == 1