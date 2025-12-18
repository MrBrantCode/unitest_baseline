"""
QUESTION:
Implement a function `is_valid_number(s: str) -> bool` that returns `true` if a given string `s` is a valid number. A valid number can be split up into these components (in order): 
- A decimal number or an integer.
- (Optional) An `'e'` or `'E'`, followed by an integer.
A decimal number can be split up into these components (in order): 
- (Optional) A sign character (either `'+'` or `'-'`).
- One of the following formats:
  - At least one digit, followed by a dot `'.'`.
  - At least one digit, followed by a dot `'.'`, followed by at least one digit.
  - A dot `'.'`, followed by at least one digit.
An integer can be split up into these components (in order): 
- (Optional) A sign character (either `'+'` or `'-'`).
- At least one digit.

Constraints: `1 <= s.length <= 20` and `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+', minus '-', or dot '.'`.
"""

import re

def is_valid_number(s: str) -> bool:
    pattern = re.compile(r'^[+-]?(\.\d+|\d+\.\d*|\d+)([eE][+-]?\d+)?$')
    return bool(pattern.match(s))