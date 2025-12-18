"""
QUESTION:
Consider the string `"adfa"` and the following rules: 
```Pearl
a) each character MUST be changed either to the one before or the one after in alphabet. 
b) "a" can only be changed to "b" and "z" to "y". 
```
From our string, we get:
```Pearl
"adfa" -> ["begb","beeb","bcgb","bceb"]
Another example: "bd" -> ["ae","ac","ce","cc"]
--We see that in each example, one of the possibilities is a palindrome.
```
I was working on the code for this but I couldn't quite figure it out. So far I have:

```python
def solve(st):
    return [all(ord(x) - ord(y) in ["FIX"] for x, y in zip(st, st[::-1]))][0]
```
I'm not sure what three numbers go into the array labelled `["FIX"]`. This is the only thing missing. 

You will be given a lowercase string and your task is to return `True` if at least one of the possiblities is a palindrome or `False` otherwise. You can use your own code or fix mine. 

More examples in test cases. Good luck!
"""

def is_palindrome_possible(st: str) -> bool:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    def generate_transformations(s: str) -> list:
        transformations = []
        for i in range(len(s)):
            char = s[i]
            if char == 'a':
                transformations.append('b')
            elif char == 'z':
                transformations.append('y')
            else:
                transformations.append(chr(ord(char) - 1))
                transformations.append(chr(ord(char) + 1))
        return transformations
    
    def backtrack(s: str, index: int, current: str) -> bool:
        if index == len(s):
            return is_palindrome(current)
        
        original_char = s[index]
        transformations = generate_transformations(original_char)
        
        for trans in transformations:
            if backtrack(s, index + 1, current + trans):
                return True
        
        return False
    
    return backtrack(st, 0, "")