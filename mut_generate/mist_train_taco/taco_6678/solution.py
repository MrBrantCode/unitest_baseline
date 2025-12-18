"""
QUESTION:
You must create a method that can convert a string from any format into CamelCase. This must support symbols too.

*Don't presume the separators too much or you could be surprised.*

### Tests
```python
camelize("example name")   # => ExampleName
camelize("your-NaMe-here") # => YourNameHere
camelize("testing ABC")    # => TestingAbc
```
"""

import re

def camelize(s: str) -> str:
    """
    Converts a given string into CamelCase format.

    Parameters:
    s (str): The input string to be converted.

    Returns:
    str: The string converted to CamelCase.
    """
    return ''.join([w.capitalize() for w in re.split('\\W|_', s)])