"""
QUESTION:
Create a function named `find_pair` that takes two parameters: an array of integers and a target sum. The function should return the first pair of numbers in the array that add up to the target sum. If no pair is found, return "No pair found". The function should work for arrays without duplicate elements.
"""

def find_pair(arr, target):
    # Create an empty hash set
    s = set()

    # Traverse through the array elements
    for i in range(0, len(arr)):
        temp = target - arr[i]
        if (temp in s):
            return arr[i], temp
        s.add(arr[i])

    return "No pair found"