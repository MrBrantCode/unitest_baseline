"""
QUESTION:
Modify the spacify function so that it returns the given string with spaces inserted between each character.

```python
spacify("hello world") # returns "h e l l o   w o r l d"
```
"""

def spacify(input_string: str) -> str:
    return ' '.join(input_string)