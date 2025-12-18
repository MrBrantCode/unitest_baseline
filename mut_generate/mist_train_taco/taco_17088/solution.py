"""
QUESTION:
Given a mathematical equation that has `*,+,-,/`, reverse it as follows:

```Haskell
solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
```

More examples in test cases. 

Good luck!

Please also try:

[Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)

[Simple remove duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)
"""

import re

def reverse_equation(eq: str) -> str:
    """
    Reverses a given mathematical equation that contains the operators `*, +, -, /`.

    Parameters:
    eq (str): The mathematical equation to be reversed.

    Returns:
    str: The reversed mathematical equation.
    """
    return ''.join(reversed(re.split('(\\W+)', eq)))