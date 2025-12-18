"""
QUESTION:
Write a function that checks the braces status in a string, and return `True` if all braces are properly closed, or `False` otherwise. Available types of brackets: `()`, `[]`, `{}`.

**Please note, you need to write this function without using regex!**

## Examples
```python
'([[some](){text}here]...)'  =>  True
'{([])}'                     =>  True
'()[]{}()'                   =>  True
'(...[]...{(..())}[abc]())'  =>  True
'1239(df){'                  =>  False
'[()])'                      =>  False
')12[x]34('                  =>  False
```
Don't forget to rate this kata! Thanks :)
"""

def check_braces_status(s: str) -> bool:
    brackets = {'}': '{', ']': '[', ')': '('}
    stack = []
    
    for c in s:
        if c in '[({':
            stack.append(c)
        elif c in '])}':
            if not stack or stack.pop() != brackets[c]:
                return False
    
    return not stack