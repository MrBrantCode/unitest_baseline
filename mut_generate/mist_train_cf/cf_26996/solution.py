"""
QUESTION:
Implement the `divide` function, which takes a list `myList` and two indices `start` and `end` as input, and partitions the list based on a pivot element. The function should rearrange the elements such that all elements less than the pivot are on the left side, and all elements greater than the pivot are on the right side. The function should return the index of the pivot element after partitioning.
"""

def divide(myList, start, end):
    pivot = myList[start]  # Choosing the first element as the pivot
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # Swap elements at myList[left] and myList[right]
            myList[left], myList[right] = myList[right], myList[left]

    # Swap pivot (myList[start]) with myList[right]
    myList[start], myList[right] = myList[right], myList[start]

    return right  # Return the index of the pivot element after partitioning