"""
QUESTION:
`late_clock` function receive an array with 4 digits and should return the latest time that can be built with those digits.
The time should be in `HH:MM` format.

Examples:
```
[1, 9, 8, 3] => 19:38
[9, 1, 2, 5] => 21:59
```

You can suppose the input is correct and you can build from it a correct 24-hour time.
"""

from itertools import permutations

def get_latest_time(digits):
    for p in permutations(sorted(digits, reverse=True)):
        if p[0] > 2 or (p[0] == 2 and p[1] > 3) or p[2] > 5:
            continue
        return '{}{}:{}{}'.format(*p)