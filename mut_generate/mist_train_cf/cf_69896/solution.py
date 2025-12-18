"""
QUESTION:
Write a function `interval_intersection` that takes two lists of closed intervals, `firstList` and `secondList`, as input and returns the intersection of these two interval lists along with the total length of the intersection intervals. 

Each list of intervals is pairwise disjoint and in sorted order. The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 

The function should handle lists with 0 to 1000 intervals, where 0 <= starti < endi <= 10^9 and 0 <= startj < endj <= 10^9. At least one of the lists should not be empty.
"""

def interval_intersection(firstList, secondList):
    i = j = 0
    result = []
    total_length = 0
    
    while i < len(firstList) and j < len(secondList):
        low = max(firstList[i][0], secondList[j][0])
        high = min(firstList[i][1], secondList[j][1])
        
        if low <= high:
            result.append([low, high])
            total_length += high - low + 1

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result, total_length