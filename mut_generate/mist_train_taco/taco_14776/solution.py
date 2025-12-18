"""
QUESTION:
Lexicographic permutations are ordered combinations of a set of items ordered in a specific way.

For instance, the first 8 permutations of the digits 0123, in lexicographic order, are:

```
1st 0123
2nd 0132
3rd 0213
4th 0231
5th 0312
6th 0321
7th 1023
8th 1032
```

Your task is to write a function ```L( n, d )``` that will return a `string` representing the `nth` permutation of the `d` digit, starting with 0 (i.e. d=10 means all digits 0123456789).

So for `d = 4`, `L(7,4)` should return `'1023'`, and `L(4,4)` should return `'0231'`
.


Some things to bear in mind:

• The function should return a `string`, otherwise permutations beginning with a 0 will have it removed. 

• Test cases will not exceed the highest possible valid values for `n`

• The function should work for any `d` between `1` and `10`.

• A value of 1 for `n` means the 1st permutation, so `n = 0` is not a valid input.

• Oh, and no itertools ;)
"""

import math

def nth_lexicographic_permutation(n, d):
    # Generate the list of digits from 0 to d-1
    digits = [str(i) for i in range(d)]
    
    # Initialize the output string
    out = ''
    
    # Adjust n to be zero-indexed
    n -= 1
    
    # Generate the nth permutation
    for i in range(1, d):
        # Calculate the number of cycles
        cycles = math.factorial(d - i)
        # Determine the index of the digit to use
        index = (n // cycles)
        # Append the selected digit to the output
        out += digits.pop(index)
        # Update n to reflect the remaining permutations
        n %= cycles
    
    # Append the last remaining digit
    out += digits.pop()
    
    return out