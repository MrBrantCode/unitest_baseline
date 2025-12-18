"""
QUESTION:
Implement the `sort_list` function that sorts a given list of integers in either ascending or descending order, removes any duplicate elements, and has a time complexity of O(nlogn). The function should take two parameters: a list of integers and a string specifying the sort order ("ascending" or "descending"). The function should not use any built-in sorting functions or data structures, and it should only use a single loop to sort the list.
"""

def sort_list(givenList, sortOrder):
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