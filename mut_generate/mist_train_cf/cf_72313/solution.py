"""
QUESTION:
Create a function `median(l: list)` that calculates the median of elements in the list `l` without sorting the list. The function should handle lists with both even and odd numbers of elements and return the median as a float for even-length lists.
"""

from heapq import *

class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

def median(l: list):
    mf = MedianFinder()
    for num in l:
        mf.addNum(num)
    return mf.findMedian()