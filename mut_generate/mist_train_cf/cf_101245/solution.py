"""
QUESTION:
Implement a function `cycleSort(array)` that sorts the input array in ascending order. The function should have a space complexity of O(1), be able to handle duplicates in the input without affecting time or space complexity, and perform the sort in-place.
"""

def cycleSort(array):
    n = len(array)
    for i in range(n-1):
        item = array[i]
        pos = i
        for j in range(i+1, n):
            if array[j] < item:
                pos += 1
        if pos == i:
            continue
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        while pos != i:
            pos = i
            for j in range(i+1, n):
                if array[j] < item:
                    pos += 1
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
    return array