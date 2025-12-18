"""
QUESTION:
Implement a function `bubble_sort(myList)` that sorts the given list `myList` in ascending order without using any built-in sorting functions or additional data structures. The list will contain unique integers with a length between 2 and 10^4 (inclusive). The solution should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort(myList):
    n = len(myList)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList