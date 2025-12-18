"""
QUESTION:
Remove the parentheses
=
In this kata you are given a string for example:

```python
"example(unwanted thing)example"
```

Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

```python
"exampleexample"
```

Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like ```"[]"``` and ```"{}"``` as these will never appear.
"""

def remove_parentheses(s: str) -> str:
    (lvl, out) = (0, [])
    for c in s:
        lvl += c == '('
        if not lvl:
            out.append(c)
        lvl -= c == ')'
    return ''.join(out)