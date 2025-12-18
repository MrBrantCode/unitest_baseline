"""
QUESTION:
Create a function called `pluck` that takes in an array of non-negative integers `arr`, a condition function `cond_fn`, and a threshold `thresh`. The function should return a list containing the smallest value in `arr` that fulfills the condition `cond_fn` and is greater than or equal to `thresh`, along with its index. If multiple values have the same smallest value, return the one with the earliest index. If no values meet the requirements, the function should return an empty list. The length of `arr` should be between 1 and 10000, the values in `arr` should be greater than or equal to 0, and `thresh` should be between -1e7 and 1e7.
"""

def pluck(arr, cond_fn, thresh):
    result = [(idx, val) for idx, val in enumerate(arr) if val >= thresh and cond_fn(val)]
    if len(result) > 0:
        result.sort(key=lambda x: (x[1], x[0]))
        return [result[0][1], result[0][0]]
    else:
        return []