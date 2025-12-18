"""
QUESTION:
You need count how many valleys you will pass.

Start is always from zero level.

Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.

One passed valley is equal one entry and one exit of a valley.
```
s='FUFFDDFDUDFUFUF'
U=UP
F=FORWARD
D=DOWN
```

To represent string above
```
(level 1)  __
(level 0)_/  \         _(exit we are again on level 0)
(entry-1)     \_     _/
(level-2)       \/\_/
```
So here we passed one valley
"""

def count_valleys(s: str) -> int:
    level = 0
    in_valley = False
    count = 0
    
    for c in s:
        if c == 'U':
            level += 1
        elif c == 'D':
            level -= 1
        
        if level >= 0 and in_valley:
            count += 1
        
        in_valley = level < 0
    
    return count