"""
QUESTION:
Create a function named "check_order" that takes a list and an optional parameter "tolerance" with a default value of 0.00001. The function should return a string indicating whether the list is sorted in ascending or descending order, or if it's not sorted. The function should be able to handle lists containing diverse data types and handle exceptions or errors that may occur during comparison.
"""

def check_order(lst, tol=0.00001):
    if len(lst) < 2:
        return "List is too short to determine sorting."

    sortedAsc = True
    sortedDesc = True

    for i in range(len(lst) - 1):

        # Handle comparison of different data types
        try:
            diff = lst[i+1] - lst[i]

        except TypeError:
            if lst[i+1] > lst[i]:
                diff = 1
            elif lst[i+1] < lst[i]:
                diff = -1
            else:
                diff = 0

        if diff < -tol:
            sortedAsc = False
        elif diff > tol:
            sortedDesc = False

        if not sortedAsc and not sortedDesc:
            return "List is not sorted."

    if sortedAsc:
        return "List is sorted in ascending order."
    elif sortedDesc:
        return "List is sorted in descending order."