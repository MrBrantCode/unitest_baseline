"""
QUESTION:
Given a list of house locations and a list of heater locations, both on a linear plane, find the smallest possible radius standard for the heaters that guarantees all houses are within the warmth radius of the heaters. The function should be named `findRadius` and take two parameters: `houses` and `heaters`. The function should return the minimum radius required. The input lists `houses` and `heaters` will have lengths between 1 and 3 * 10^4, and the values in the lists will be between 1 and 10^9.
"""

import bisect

def findRadius(houses, heaters):
    heaters.sort()
    ans = 0
            
    for h in houses:
        hi = bisect.bisect(heaters, h)
        left = heaters[hi-1] if hi-1 >= 0 else float('-inf')
        right = heaters[hi] if hi < len(heaters) else float('inf')
        ans = max(ans, min(abs(h-right), abs(h-left)))
        
    return ans