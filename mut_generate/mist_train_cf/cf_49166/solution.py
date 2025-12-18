"""
QUESTION:
Implement a function named `move_zeros` that takes an array as input and returns a modified array where all occurrences of the integer zero are moved to the end of their respective array/subarrays while maintaining the order of other elements. The function should handle arrays of any depth, arrays with multiple data types, circular arrays, and large arrays (up to 10^6 elements) efficiently. The function should also return the original array if there are no zeros present.
"""

def move_zeros(arr):
    #check if arr is a list
    if type(arr) != list:
        return arr
    #otherwise
    zero_counter = arr.count(0)
    new_arr = [i for i in arr if i != 0 or type(i) != int] 
    return new_arr + [0]*zero_counter