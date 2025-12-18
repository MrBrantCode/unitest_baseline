"""
QUESTION:
Construct a function that, when given a string containing an expression in infix notation, will return an identical expression in postfix notation.

The operators used will be `+`, `-`, `*`, `/`, and `^` with standard precedence rules and left-associativity of all operators but `^`.

The operands will be single-digit integers between 0 and 9, inclusive.

Parentheses may be included in the input, and are guaranteed to be in correct pairs.

```javascript 
toPostfix("2+7*5"); // Should return "275*+"
toPostfix("3*3/(7+1)"); // Should return "33*71+/"
toPostfix("5+(6-2)*9+3^(7-1)"); // Should return "562-9*+371-^+"
```
```python
to_postfix("2+7*5") # Should return "275*+"
to_postfix("3*3/(7+1)") # Should return "33*71+/"
to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
```

You may read more about postfix notation, also called Reverse Polish notation, here:
http://en.wikipedia.org/wiki/Reverse_Polish_notation
"""

def infix_to_postfix(infix_expression: str) -> str:
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    postfix = []
    stack = []
    
    for ch in infix_expression:
        if ch in '0123456789':
            postfix.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prec[stack[-1]] >= prec[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)