"""
QUESTION:
You are given an array of integer intervals `intervals` where each interval is in the form `[a, b]` (for integers `a < b`). The task is to find the maximum size of a set `S` such that for every integer interval `A` in `intervals`, the union of `S` with `A` has a size of at most two.

The function to solve this problem is `intersectionSizeTwo(intervals)`. The input is an array of integer intervals, and the output is the maximum size of the set `S`.

The constraints are:
- `1 <= intervals.length <= 3000`
- `intervals[i].length == 2`
- `0 <= ai < bi <= 10^8`
"""

def intersectionSizeTwo(intervals):
    intervals.sort(key=lambda x: (x[1], -x[0]))
    todo = [2] * len(intervals)
    ans = 0
    while todo:
        targ = todo.pop()
        for s in range(targ-1, -1, -1):
            for i in reversed(range(len(todo))): 
                if todo[i] <= 0 or (intervals[i][0] <= s < intervals[i][1]):
                    todo[i] -= 1
                    ans += 1
                    break
            else: continue
            break
    return ans