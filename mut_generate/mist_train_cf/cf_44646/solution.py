"""
QUESTION:
Write a function `maxBoxesInWarehouse(boxes, warehouse)` that takes two lists of positive integers `boxes` and `warehouse` as input and returns the maximum number of boxes that can be accommodated in the warehouse. 

The `boxes` list represents the heights of some boxes of unit width, and the `warehouse` list represents the heights of `n` rooms in a warehouse. The rules for placing boxes into the warehouse are as follows: 
- Boxes cannot be stacked.
- The sequence of box insertion can be rearranged.
- Boxes can be inserted into the warehouse from either side (left or right).
- If a room's height in the warehouse is less than the height of a box, then that box and all other boxes behind it will be halted before that room.

The constraints for the function are:
`n == warehouse.length`
`1 <= boxes.length, warehouse.length <= 10^5`
`1 <= boxes[i], warehouse[i] <= 10^9`
"""

def maxBoxesInWarehouse(boxes, warehouse):
    boxes.sort(reverse=True)
    l = 0
    r = len(warehouse) - 1
    i = 0
    count = 0
    while l <= r and i < len(boxes):
        if boxes[i] <= warehouse[l]:
            l += 1
            count += 1
        elif boxes[i] <= warehouse[r]:
            r -= 1
            count += 1
        i += 1
    return count