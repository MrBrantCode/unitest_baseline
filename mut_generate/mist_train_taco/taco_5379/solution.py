"""
QUESTION:
Assume `"#"` is like a backspace in string. This means that string `"a#bc#d"` actually is `"bd"`

Your task is to process a string with `"#"` symbols.


## Examples

```
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
```
"""

def process_string_with_backspaces(s: str) -> str:
    stk = []
    for c in s:
        if c == '#' and stk:
            stk.pop()
        elif c != '#':
            stk.append(c)
    return ''.join(stk)