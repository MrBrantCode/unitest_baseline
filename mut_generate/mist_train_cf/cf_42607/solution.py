"""
QUESTION:
Write a function `find_median(data)` that takes a list of integers `data` as input and returns the median of the list. The median is the middle value in a sorted list of numbers. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def find_median(data):
    data.sort()
    length = len(data)
    if length % 2 == 1:
        return data[length // 2]
    else:
        mid1 = data[length // 2 - 1]
        mid2 = data[length // 2]
        return (mid1 + mid2) / 2