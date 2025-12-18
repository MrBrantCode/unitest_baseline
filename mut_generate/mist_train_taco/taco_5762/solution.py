"""
QUESTION:
In this Kata, you will be given a mathematical string and your task will be to remove all braces as follows:

```Haskell
solve("x-(y+z)") = "x-y-z"
solve("x-(y-z)") = "x-y+z"
solve("u-(v-w-(x+y))-z") = "u-v+w+x+y-z"
solve("x-(-y-z)") = "x+y+z"
```

There are no spaces in the expression. Only two operators are given: `"+" or "-"`. 

More examples in test cases. 

Good luck!
"""

from functools import reduce

def simplify_expression(expression: str) -> str:
    res, s, k = [], '', 1
    for ch in expression:
        if ch == '(':
            res.append(k)
            k = 1
        elif ch == ')':
            res.pop()
            k = 1
        elif ch == '-':
            k = -1
        elif ch == '+':
            k = 1
        else:
            s += '-' + ch if reduce(lambda a, b: a * b, res, 1) * (1 if k == 1 else -1) < 0 else '+' + ch
    return s if s[0] == '-' else s[1:]