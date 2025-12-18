"""
QUESTION:
Write a simple parser that will parse and run Deadfish.  

Deadfish has 4 commands, each 1 character long:
* `i` increments the value (initially `0`)
* `d` decrements the value
* `s` squares the value
* `o` outputs the value into the return array

Invalid characters should be ignored.

```python
parse("iiisdoso")  ==>  [8, 64]
```
"""

def parse_deadfish(data: str) -> list[int]:
    value = 0
    res = []
    for c in data:
        if c == 'i':
            value += 1
        elif c == 'd':
            value -= 1
        elif c == 's':
            value *= value
        elif c == 'o':
            res.append(value)
    return res