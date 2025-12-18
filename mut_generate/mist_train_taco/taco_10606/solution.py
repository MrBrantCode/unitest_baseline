"""
QUESTION:
Complete the solution so that it takes the object (JavaScript/CoffeeScript) or hash (ruby) passed in and generates a human readable string from its key/value pairs. 

The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.

**Example:**
```python
solution({"a": 1, "b": '2'}) # should return "a = 1,b = 2"
```
"""

def generate_readable_string(pairs):
    """
    Generates a human-readable string from the key-value pairs in the given dictionary.

    Parameters:
    pairs (dict): A dictionary containing key-value pairs.

    Returns:
    str: A string formatted as "KEY = VALUE" with each key-value pair separated by a comma.
    """
    return ','.join(sorted(f'{k} = {pairs[k]}' for k in pairs))