"""
QUESTION:
Implement a function `sort_list(givenList, sortOrder)` that takes a list of integers `givenList` and a string `sortOrder` ("ascending" or "descending") as input. The function should return the sorted list without any duplicate elements. The function should not use any built-in sorting functions or data structures and should have a time complexity of O(nlogn).
"""

def entrance(givenList, sortOrder):
    # Remove duplicates
    givenList = list(set(givenList))
    
    # Sort the list in ascending order
    if sortOrder == "ascending":
        for i in range(len(givenList)):
            for j in range(len(givenList)-1-i):
                if givenList[j] > givenList[j+1]:
                    givenList[j], givenList[j+1] = givenList[j+1], givenList[j]
    
    # Sort the list in descending order
    elif sortOrder == "descending":
        for i in range(len(givenList)):
            for j in range(len(givenList)-1-i):
                if givenList[j] < givenList[j+1]:
                    givenList[j], givenList[j+1] = givenList[j+1], givenList[j]
    
    return givenList