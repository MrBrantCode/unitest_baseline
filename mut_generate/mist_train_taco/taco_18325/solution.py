"""
QUESTION:
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return `true` if the string is valid, and `false` if it's invalid.

This Kata is similar to the [Valid Parentheses](https://www.codewars.com/kata/valid-parentheses) Kata, but introduces new characters: brackets `[]`, and curly braces `{}`. Thanks to `@arnedag` for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: `()[]{}`. 


### What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.


## Examples

```
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
```
"""

def is_valid_braces(braces_string: str) -> bool:
    """
    Determines if the order of the braces in the given string is valid.

    Args:
        braces_string (str): The string containing the braces to be validated.

    Returns:
        bool: True if the string of braces is valid, False otherwise.
    """
    braces_map = {'(': ')', '[': ']', '{': '}'}
    stack = []
    
    for char in braces_string:
        if char in braces_map.keys():
            stack.append(char)
        elif len(stack) == 0 or braces_map[stack.pop()] != char:
            return False
    
    return len(stack) == 0