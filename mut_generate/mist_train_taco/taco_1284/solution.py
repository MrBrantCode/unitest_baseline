"""
QUESTION:
Write a function that gets a sequence and value and returns `true/false` depending on whether the variable exists in a multidimentional sequence.

Example:
```
locate(['a','b',['c','d',['e']]],'e'); // should return true
locate(['a','b',['c','d',['e']]],'a'); // should return true
locate(['a','b',['c','d',['e']]],'f'); // should return false
```
"""

def is_value_in_sequence(seq, value):
    for s in seq:
        if s == value or (isinstance(s, list) and is_value_in_sequence(s, value)):
            return True
    return False