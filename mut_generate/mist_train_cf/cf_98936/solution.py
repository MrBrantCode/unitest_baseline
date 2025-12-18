"""
QUESTION:
Implement a function called `cycleSort(array)` that sorts the input array in ascending order using the Cycle Sort algorithm, maintaining a space complexity of O(1) and handling duplicates without affecting time or space complexity. The function should perform the sort in-place and return the sorted array.
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