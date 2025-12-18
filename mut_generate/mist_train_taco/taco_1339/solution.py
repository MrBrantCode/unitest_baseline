"""
QUESTION:
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= input.length <= 100`

~~~if-not:javascript,go
Along with opening (`(`) and closing (`)`) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do **not** treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
~~~
"""

def is_valid_parentheses(input_string: str) -> bool:
    cnt = 0
    for char in input_string:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0