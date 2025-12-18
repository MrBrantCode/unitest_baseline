"""
QUESTION:
Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis. 

For example:
```Javascript
solve(")(") = 2 Because we need to reverse ")" to "(" and "(" to ")". These are 2 reversals. 
solve("(((())") = 1 We need to reverse just one "(" parenthesis to make it balanced.
solve("(((") = -1 Not possible to form balanced parenthesis. Return -1.
```

Parenthesis will be either `"("` or `")"`. 

More examples in the test cases. 

Good luck.
"""

def min_parenthesis_reversals(s: str) -> int:
    # Remove all balanced pairs of parentheses
    t = None
    while t != s:
        t, s = s, s.replace('()', '')
    
    # If the length of the remaining string is odd, it's not possible to balance
    if len(s) % 2 != 0:
        return -1
    
    # Calculate the number of reversals needed
    reversals = sum(1 + (a == tuple(')(')) for a in zip(*[iter(s)] * 2))
    return reversals