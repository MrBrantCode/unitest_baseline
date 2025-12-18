"""
QUESTION:
Write a function called "computeWays" that takes in two parameters: a list of unique items and an integer k, where k is the number of items to be selected from the list and k <= n. The function should return the total number of ways to select k items from the list.
"""

def computeWays(options, k):
    totalWays = 0

    def selectItems(index, selectedCount, selectedIDs):
        nonlocal totalWays

        if selectedCount == k:
            totalWays += 1
            return
        
        if index == len(options):
            return

        selectItems(index + 1, selectedCount, selectedIDs)
        selectItems(index + 1, selectedCount + 1, selectedIDs + [options[index]])

    selectItems(0, 0, [])
    return totalWays