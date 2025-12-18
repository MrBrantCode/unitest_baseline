"""
QUESTION:
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

## Example:

```python
past(0, 1, 1) == 61000
```

Input constraints: `0 <= h <= 23`, `0 <= m <= 59`, `0 <= s <= 59`
"""

def convert_time_to_milliseconds(h: int, m: int, s: int) -> int:
    return (3600 * h + 60 * m + s) * 1000