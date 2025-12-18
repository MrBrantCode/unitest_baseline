"""
QUESTION:
Your job is to change the given string `s` using a non-negative integer `n`.

Each bit in `n` will specify whether or not to swap the case for each alphabetic character in `s`: if the bit is `1`, swap the case; if its `0`, leave it as is. When you finished with the last bit of `n`, start again with the first bit.

You should skip the checking of bits when a non-alphabetic character is encountered, but they should be preserved in their original positions.

## Examples

```
swap('Hello world!', 11)  -->  'heLLO wORLd!'
```
...because `11` is `1011` in binary, so the 1st, 3rd, 4th, 5th, 7th, 8th and 9th alphabetical characters have to be swapped:
```
H e l l o  w o r l d !
1 0 1 1 1  0 1 1 1 0
^   ^ ^ ^    ^ ^ ^
```

More examples:
```
swap("gOOd MOrniNg", 7864)  -->  "GooD MorNIng"
swap('', 11345)  -->  ''
swap('the lord of the rings', 0)  -->  'the lord of the rings'
```
"""

from itertools import cycle

def swap_case_by_bits(s: str, n: int) -> str:
    # Convert the integer n to its binary representation and cycle through its bits
    bit_cycle = cycle(bin(n)[2:])
    
    # Iterate through each character in the string s
    result = ''.join(
        c.swapcase() if c.isalpha() and next(bit_cycle) == '1' else c
        for c in s
    )
    
    return result