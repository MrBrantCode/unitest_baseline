"""
QUESTION:
Create a function `find_median` that takes two lists of integers as input, combines them into a single list, removes duplicates, sorts the list in ascending order, and returns the median of the sorted list. If the length of the list is even, the median is the average of the two middle numbers. The function should not take any additional parameters other than the two input lists.
"""

def find_median(List1, List2):
    mergedList = List1 + List2
    dedupList = list(set(mergedList))
    sortedList = sorted(dedupList)
    
    length = len(sortedList)
    
    if length % 2 == 0:
        median = (sortedList[length//2] + sortedList[length//2 - 1]) / 2
    else:
        median = sortedList[length//2]
        
    return median