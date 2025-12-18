"""
QUESTION:
You are given two arrays of positive integers, `boxes` and `warehouse`, representing the heights of boxes and rooms in a warehouse respectively. Your task is to determine the maximum number of boxes that can be accommodated in the warehouse, where boxes cannot be stacked, the sequence of box insertion can be rearranged, and boxes can only be inserted from left to right. The function `maxBoxesInWarehouse(boxes, warehouse)` should return the maximum number of boxes that can be accommodated. The length of both `boxes` and `warehouse` is between 1 and 10^5, and the height of each box and room is between 1 and 10^9.
"""

def maxBoxesInWarehouse(boxes, warehouse):
    boxes.sort(reverse=True)
    warehouse.sort(reverse=True)
    i = j = 0
    while i < len(boxes) and j < len(warehouse):
        if boxes[i] <= warehouse[j]:
            i += 1
        j += 1
    return i