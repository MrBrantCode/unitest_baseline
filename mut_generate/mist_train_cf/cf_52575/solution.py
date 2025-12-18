"""
QUESTION:
Create a function `max_divide_conquer(arr, start, end)` that finds the maximum value in an array using the divide and conquer technique. The function should take as input an array `arr` and two indices `start` and `end` representing the range of the array to be considered. The function should return the maximum value in the specified range of the array.
"""

def max_divide_conquer(arr, start, end): 
    #If the array contains only one element.
    if start==end: 
        return arr[start]
  
    #Find the middle point.  
    mid = (start+end)//2
    
    #The maximum value will be the maximum between the maximum values of the two halves.
    max_in_first_half = max_divide_conquer(arr, start, mid) 
    max_in_second_half = max_divide_conquer(arr, mid+1, end)
    
    return max(max_in_first_half, max_in_second_half)