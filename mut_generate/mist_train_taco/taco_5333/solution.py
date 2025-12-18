"""
QUESTION:
Given an integer `n` return `"odd"` if the number of its divisors is odd. Otherwise return `"even"`.

**Note**: big inputs will be tested.

## Examples:

All prime numbers have exactly two divisors (hence `"even"`).

For `n = 12` the divisors are `[1, 2, 3, 4, 6, 12]` – `"even"`.

For `n = 4` the divisors are `[1, 2, 4]` – `"odd"`.
"""

def determine_divisor_oddity(n: int) -> str:
    return 'odd' if n ** 0.5 == int(n ** 0.5) else 'even'