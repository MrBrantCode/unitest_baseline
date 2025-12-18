"""
QUESTION:
Write a function `find_max_subarray_sum` that takes a two-dimensional array as input and returns the maximum sum of any subarray within the array. The array can have up to 1000 rows and 1000 columns, and the values in the array can range from -10^9 to 10^9.
"""

def find_max_subarray_sum(array):
    max_sum = 0
    global_max_sum = 0

    for row in array:
        current_sum = 0

        for num in row:
            current_sum += num

            if current_sum < 0:
                current_sum = 0

            if current_sum > max_sum:
                max_sum = current_sum

        if max_sum > global_max_sum:
            global_max_sum = max_sum

    return global_max_sum