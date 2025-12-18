"""
QUESTION:
Write a function `max_disparity(two_dim_arr)` that calculates the maximum disparity between the smallest and the largest elements in each sub-array of a given two-dimensional integer array. The function should return a list of disparities for all non-empty sub-arrays.
"""

def max_disparity(two_dim_arr):
    disparity_list = []
  
    for sub_arr in two_dim_arr:
        if len(sub_arr) > 0:   
            min_val = sub_arr[0]
            max_val = sub_arr[0]
            for num in sub_arr:
                min_val = min(min_val,num)
                max_val = max(max_val,num)
            disparity_list.append(max_val - min_val)
    return disparity_list