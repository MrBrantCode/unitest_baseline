"""
QUESTION:
Consider the following expansion:
```Haskell
solve("3(ab)") = "ababab" -- "ab" repeats 3 times
solve("2(a3(b))" = "abbbabbb" -- "a3(b)" == "abbb" repeats twice.
```

Given a string, return the expansion of that string. 

Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis. There will be no letters or numbers after the last closing parenthesis.

More examples in test cases. 

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
"""

def expand_string(s: str) -> str:
    def expand_helper(s: str) -> str:
        stack = []
        current_string = ""
        current_number = ""
        
        for char in s:
            if char.isdigit():
                current_number += char
            elif char == '(':
                if current_number:
                    stack.append(int(current_number))
                    current_number = ""
                stack.append(current_string)
                current_string = ""
            elif char == ')':
                while stack and not isinstance(stack[-1], int):
                    current_string = stack.pop() + current_string
                if stack and isinstance(stack[-1], int):
                    repeat_count = stack.pop()
                    current_string *= repeat_count
            else:
                current_string += char
        
        while stack:
            current_string = stack.pop() + current_string
        
        return current_string
    
    return expand_helper(s)