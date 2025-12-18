"""
QUESTION:
Write a function `str_without_3a3b3c(a: int, b: int, c: int) -> str` that takes three integers `a`, `b`, and `c` and returns any string `s` such that:
- `s` has length `a + b + c` and contains exactly `a` 'a' letters, exactly `b` 'b' letters, and exactly `c` 'c' letters.
- The substring 'aaa', 'bbb', or 'ccc' does not occur in `s`.
- The substring 'abc' does not occur in `s`.

Constraints: `0 <= a, b, c <= 100`. It is guaranteed such an `s` exists for the given `a`, `b`, and `c`.
"""

def str_without_3a3b3c(a: int, b: int, c: int) -> str:
    result = []
    counts = [['a', a], ['b', b], ['c', c]]

    while any(count[1] > 0 for count in counts):
        # Sort to get char with max remaining count as the last element
        counts.sort(key=lambda x: x[1])

        # Avoid selecting the same char 3 times in a row
        if len(result) >= 2 and result[-1] == result[-2] == counts[-1][0]:
            if counts[-2][1] <= 0:
                return ''   # No valid string possible
            counts[-2][1] -= 1
            result.append(counts[-2][0])
        else:
            counts[-1][1] -= 1
            result.append(counts[-1][0])

    return ''.join(result)