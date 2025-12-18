"""
QUESTION:
Write a function `maximumScore(s, x, y, z, w)` that takes a string `s` and four integers `x`, `y`, `z`, and `w` as input. Return the maximum points that can be gained by removing substrings 'ab', 'ba', 'abc', and 'abcd' from `s` and getting points `x`, `y`, `z`, and `w` respectively. The string `s` consists of lowercase English letters and its length is between 1 and 10^5. The values of `x`, `y`, `z`, and `w` are between 1 and 10^4.
"""

def maximumScore(s, x, y, z, w):
    score = 0
    cnt_a, cnt_b = 0, 0
    s += " "
    for i in range(len(s)):
        if s[i] == 'a':
            cnt_a += 1
        elif s[i] == 'b':
            if cnt_a > 0 and x + y < z and i + 2 < len(s) and s[i + 2] == 'c':
                cnt_a -= 1
                score += z
            elif cnt_a > 0 and x > y:
                cnt_a -= 1
                score += x
            else:
                cnt_b += 1
        elif s[i] == 'c':
            if cnt_b > 0 and i + 1 < len(s) and s[i + 1] == 'd' and w > z:
                cnt_b -= 1
                score += w
                i += 1
            elif cnt_b > 0:
                cnt_b -= 1
                score += z
    return score + cnt_a * x + cnt_b * y