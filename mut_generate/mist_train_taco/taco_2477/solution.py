"""
QUESTION:
# Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

## Example:

```
348597 => [7,9,5,8,4,3]
```
"""

def convert_number_to_reversed_digits(n: int) -> list[int]:
    return [int(x) for x in str(n)[::-1]]