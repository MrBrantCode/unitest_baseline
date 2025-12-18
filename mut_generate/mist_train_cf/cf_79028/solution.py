"""
QUESTION:
Create a function `getNextElement(lst, elem)` that returns the next element in a list after the given element `elem`. If `elem` is the last element in the list, the function should return the first element. If `elem` is not in the list, the function should return `None`.
"""

def getNextElement(lst, elem):
    try:
        indx = lst.index(elem)
    except ValueError:
        return None
    if indx == len(lst)-1:
        # If the element is the last in the list, return the first one
        return lst[0]
    else:
        return lst[indx+1]