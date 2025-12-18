"""
QUESTION:
Write a function `array_properties` that takes an arbitrary array `arr` as input, prints its length, and prints the middle element(s). If the array has an even number of elements, it should print the two middle elements. The function should also handle the edge case where the array is empty, in which case it should print a corresponding message.
"""

def array_properties(arr):
    length = len(arr)
    
    #Handle edge case for empty array
    if length == 0:
        print("The array is empty.")
        return 

    if length % 2 == 0:
        # - 1 is necessary because list indices start with 0
        mid = arr[length//2 - 1 : length//2 + 1]
    else:
        mid = arr[length//2]

    print("Length:", length, "Middle Element(s):", mid)