"""
QUESTION:
Function `longestBridge(beams)`: Return the longest possible length of a bridge construction with two equal-length concrete supports from a given collection of beams. The function should return 0 if the bridge cannot be supported.

Given information:
- `beams` is a list of integers representing the lengths of the beams.
- The length of the `beams` list is between 1 and 20 (inclusive).
- The length of each beam is between 1 and 1000 (inclusive).
- The sum of the lengths of all beams is less than 5000.

The function should return the maximum possible length of the bridge with equal-length concrete supports.
"""

def longestBridge(beams):
    def dp(idx, a, b):
        if idx == len(beams):
            if a == b:
                return a
            else:
                return 0
        else:
            return max(dp(idx+1, a+beams[idx], b), dp(idx+1, a, b+beams[idx]), dp(idx+1, a, b))

    return dp(0, 0, 0)