"""
QUESTION:
You are given an array of `n` strings `strs`, all of the same length, which can be arranged as a grid. Return the minimum number of columns that need to be deleted to make the remaining columns sorted lexicographically.

Constraints: 
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 1000`
- `strs[i]` consists of lowercase English letters.
- The strings in `strs` may contain duplicate characters.

Function name: `minDeletionSize(strs)`
"""

def minDeletionSize(strs):
    ans = 0
    cur = [""] * len(strs)

    for j in map(list, zip(*strs)):
        cur2 = [c + j[i] for i, c in enumerate(cur)]
        if all(cur2[i] >= cur2[i-1] for i in range(1, len(cur2))):
            cur = cur2
        else:
            ans += 1

    return ans