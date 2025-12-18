"""
QUESTION:
Write a function called `reverse_arr` that takes an array of integers as input. The function should return the array with all positive numbers in reverse order while maintaining the original positions of negative numbers and zeros. If there are no positive numbers in the array, return the string "Cannot reverse the order of the given integers".
"""

def reverse_arr(arr):
    negs_and_zeros = [x for x in arr if x <= 0]
    positives = [x for x in arr if x > 0]
    
    if not positives:   # if there are no positive numbers
        return "Cannot reverse the order of the given integers"
        
    pos_counter = len(positives) - 1   # start from the end of positive numbers
    output_arr = []
    
    for x in arr:
        if x > 0:
            output_arr.append(positives[pos_counter])
            pos_counter -= 1   # move to the previous positive number
        else:
            output_arr.append(x)   # if it's not positive, append as is
            
    return output_arr