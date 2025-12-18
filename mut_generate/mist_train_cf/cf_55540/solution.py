"""
QUESTION:
Write a function `maximumUnits` that takes a 2D array `boxTypes` and an integer `truckSize` as input and returns the maximum possible total number of units that can be loaded onto the truck. `boxTypes[i]` represents the quantity and number of units per box of type `i`, and `truckSize` denotes the maximum capacity of boxes the truck can accommodate. The function should return an integer representing the maximum total units. The constraints are `1 <= boxTypes.length <= 1000`, `1 <= boxTypes[i][0], boxTypes[i][1] <= 1000`, and `1 <= truckSize <= 10^6`.
"""

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key = lambda x:-x[1])
    count = 0
    for box in boxTypes:
        if truckSize >= box[0]:
            count += box[0] * box[1]
            truckSize -= box[0]
        else:
            count += truckSize * box[1]
            return count
    return count