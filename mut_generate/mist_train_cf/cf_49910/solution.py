"""
QUESTION:
Write a regular expression to match strings containing one or more sequences of exactly three uppercase letters followed by exactly two lowercase letters, without overlapping matches. The regular expression should be as efficient as possible. Implement the solution in Python.
"""

import re

def entrance(upper, lower):
    return re.compile(r'[A-Z]{'+str(upper)+'}[a-z]{'+str(lower)+'}')

# The function can be used like this:
# regex = entrance(3, 2)