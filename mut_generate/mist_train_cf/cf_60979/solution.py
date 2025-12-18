"""
QUESTION:
Given a string `s` and three integers `x`, `y`, and `z`, write a function `maximumGain` to return the maximum points that can be gained after applying the following operations on `s`: remove substring `"ab"` to gain `x` points, remove substring `"ba"` to gain `y` points, and remove substring `"abc"` to gain `z` points. The function should work under the following constraints: `1 <= s.length <= 10^5`, `1 <= x, y, z <= 10^4`, and `s` consists of lowercase English letters.
"""

def maximumGain(s: str, x: int, y: int, z: int) -> int:
    s = '#'+s+'#'
    ans = 0
    a = b = 0
    for ch in s:
        if ch == 'a':
            a += 1
        elif ch == 'b':
            b += 1
            if a > 0 and x >= y:
                a -= 1
                b -= 1
                ans += x
        elif ch == 'c':
            min_ab = min(a, b)
            ans += min_ab * z
            a -= min_ab
            b -= min_ab
            if x >= y:
                b = 0
            else:
                a = 0
        else:
            ans += min(a, b) * min(x, y)
            a = b = 0
    ans += min(a, b) * min(x, y)
    return ans