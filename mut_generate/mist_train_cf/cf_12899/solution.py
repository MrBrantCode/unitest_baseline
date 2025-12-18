"""
QUESTION:
Find all duplicates in an array of positive integers where each integer is between 1 and 100, inclusive. The array may contain up to 10^6 elements. The function should return the duplicates in ascending order. 

Create a function named 'findDuplicates' that takes an array of integers as input and returns a list of duplicate integers in ascending order.
"""

def findDuplicates(arr):
    counts = {}  # dictionary to store the count of each number
    duplicates = []  # list to store the duplicates

    # iterate through the array and count each number
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # iterate through the dictionary and add duplicates to the list
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)

    # sort the list in ascending order and return it
    duplicates.sort()
    return duplicates