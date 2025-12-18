"""
QUESTION:
Write a function `find_target(nums, value)` that takes a 2D array `nums` and a target integer `value` as input. The function should return the number of occurrences of `value` in `nums` as a string. If `value` is not found, return a message stating so. The function should handle 2D arrays with up to 10,000 elements per array, with numbers ranging from -10,000 to 10,000, and should complete within 1 second.
"""

def find_target(nums, value):
    count = 0
    for array in nums:
        for num in array:
            if num == value:
                count += 1
    if count:  
        return 'The target (' + str(value) + ') is present ' + str(count) + ' times.'
    else:
        return 'The target ' + str(value) + ' is not present in the list.'