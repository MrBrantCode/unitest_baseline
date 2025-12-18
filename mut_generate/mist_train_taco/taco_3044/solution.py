"""
QUESTION:
## Task

Given a positive integer as input, return the output as a string in the following format: 

Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.

## Examples

Input | Output
---   | ---
0     | ""
56    | "5\*10+6"
60    | "6\*10"
999   | "9\*100+9\*10+9"
10004 | "1\*10000+4"

Note: `input >= 0`
"""

def simplify_number(n: int) -> str:
    output = []
    exp = 0
    while n:
        (n, r) = divmod(n, 10)
        if r:
            output.append(f'{r}*{10 ** exp}' if exp else f'{r}')
        exp += 1
    return '+'.join(output[::-1])