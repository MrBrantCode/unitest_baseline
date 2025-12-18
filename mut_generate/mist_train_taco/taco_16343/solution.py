"""
QUESTION:
Given a string `s` of uppercase letters, your task is to determine how many strings `t` (also uppercase) with length equal to that of `s` satisfy the followng conditions:

* `t` is lexicographical larger than `s`, and
* when you write both `s` and `t` in reverse order, `t` is still lexicographical larger than `s`.


```Haskell
For example:
solve('XYZ') = 5. They are: YYZ, ZYZ, XZZ, YZZ, ZZZ
```
String lengths are less than `5000`. Return you answer `modulo 10^9+7 (= 1000000007)`.

More examples in test cases. Good luck!
"""

def count_lexicographical_larger_reversed(s: str) -> int:
    MOD = 1000000007
    r, l = 0, 0
    for c in s:
        m = ord('Z') - ord(c)
        r, l = (r + m + l * m) % MOD, (m + l * 26) % MOD
    return r