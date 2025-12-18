"""
QUESTION:
Create a function called "computeWays" that takes in two parameters: a list of unique items and the number of items to select (k), where k is less than or equal to the total number of items. The function should return the total number of ways to select k items from the list.
"""

def computeWays(options, k):
    def selectItems(index, selected):
        if selected == k:
            return 1
        if index == len(options):
            return 0
        
        return selectItems(index + 1, selected) + selectItems(index + 1, selected + 1)
    
    return selectItems(0, 0)