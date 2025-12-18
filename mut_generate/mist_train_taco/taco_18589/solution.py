"""
QUESTION:
Related to MrZizoScream's Product Array kata. You might want to solve that one first :)

```if:javascript
**Note:** Node 10 has now been enabled, and you can now use its BigInt capabilities if you wish, though your resulting array must still contain strings (e.g. "99999999999", not 9999999999n)

Pre-node 10: You will need to use the BigNumber.js library! Please use `.toFixed(0)` or `.toPrecision()` to round instead of `.toString(10)`, as the latter is _very_ slow
```

This is an adaptation of a problem I came across on LeetCode. 

Given an array of numbers, your task is to return a new array where each index (`new_array[i]`) is equal to the product of the original array, except for the number at that index (`array[i]`).

**Two things to keep in mind:**

* Zeroes will be making their way into some of the arrays you are given
* O(n^2) solutions will not pass.

Examples:

**Note**: All inputs will be valid arrays of nonzero length.

Have fun! Please upvote if you enjoyed :)
"""

from functools import reduce

def product_array_except_self(nums):
    z = nums.count(0)
    if z > 1:
        return ['0'] * len(nums)
    p = reduce(int.__mul__, (v for v in nums if v))
    if z:
        return [str(p) if v == 0 else '0' for v in nums]
    else:
        return [str(p // v) for v in nums]