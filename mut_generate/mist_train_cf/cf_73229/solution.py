"""
QUESTION:
Design a function `sortArrayInRangeWithQueries` that takes an array of integers and a list of range queries as input. The function should sort all elements within the given ranges in the array using the cocktail shaker sorting methodology, leaving elements outside the ranges unchanged. The ranges are inclusive, with indices starting from 1. Implement valid range checks to handle invalid queries.

The function should take two parameters: `arr` (the input array) and `queries` (a list of tuples representing the range queries). If any invalid range is encountered, print an error message and return the original array. Otherwise, return the modified array with the elements sorted within the specified ranges.
"""

def sortArrayInRangeWithQueries(arr, queries):
    def cocktailShakerSort(inputList, startIndex, endIndex):
        n = endIndex - startIndex + 1

        # Start & end pointers for the array.
        start = 0
        end = n-1
        swapped = True

        while (swapped==True):

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # Loop from left to right
            for i in range (start, end):
                if (inputList[startIndex + i] > inputList[startIndex + i + 1]):
                    inputList[startIndex + i], inputList[startIndex + i+1]= inputList[startIndex + i + 1], inputList[startIndex + i]
                    swapped=True

            # if nothing moved, then array is sorted.
            if (swapped==False):
                break

            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end-1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end-1, start-1,-1):
                if (inputList[startIndex + i] > inputList[startIndex + i + 1]):
                    inputList[startIndex + i], inputList[startIndex + i + 1] = inputList[startIndex + i + 1], inputList[startIndex + i]
                    swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1

    #Checking for valid range queries
    for (start, end) in queries:
        if start < 1 or end > len(arr):
            print(f'Invalid range [{start}, {end}]')
            return arr
    
    for (start, end) in queries:
        cocktailShakerSort(arr, start-1, end-1)
    
    return arr