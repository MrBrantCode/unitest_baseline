"""
QUESTION:
Implement a stable sorting algorithm, called `bucketSort`, that can handle negative and floating point numbers and runs in linear time. The function should take an array of numbers as input and return the sorted array. The algorithm should be able to distribute the input data into buckets, sort each bucket, and then combine the sorted buckets to get the final sorted array. The bucket size should be adjustable, with a default value of 0.1.
"""

def bucketSort(array, bucketSize=0.1):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Initialize buckets
    bucketCount = int((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input data into buckets
    for i in range(0, len(array)):
        buckets[int((array[i] - minValue) / bucketSize)].append(array[i])

    # Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key