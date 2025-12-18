"""
QUESTION:
Write a function `find_odd_occurrences` that takes a multidimensional array of integers as input and returns a dictionary. The function should iterate over each sub-array, calculate the index of the element that occurs an odd number of times, and store the index of the sub-array as the key and the index of the odd occurring element as the value in the dictionary. If no element in a sub-array appears an odd number of times, the value of the dictionary should be -1.
"""

def find_odd_occurrences(arr):
    result = {} # initialize an empty dictionary
    for i, sub_arr in enumerate(arr):
        counter = {} # initialize a counter dictionary
        for j, num in enumerate(sub_arr): 
            counter[num] = counter.get(num, 0) + 1 # update the count of the number
        for num, count in counter.items():
            if count % 2 != 0:  # check if the count is odd.
                result[i] = sub_arr.index(num) # if yes, store the index of the sub-array and the index of the number
                break 
        else: 
            result[i] = -1 # if not, store -1
    return result