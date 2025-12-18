"""
QUESTION:
Create a function called `round_array` that takes an array of real numbers as input and returns a new array where each number is rounded to its nearest integer, rounding up if the fractional part is greater than 0.5 and rounding down if it is less than or equal to 0.5. The function must have a time complexity of O(n), where n is the length of the input array.
"""

def round_array(arr):
    rounded_array = []
    for num in arr:
        rounded_num = int(num)
        if num - rounded_num > 0.5:
            rounded_num += 1
        rounded_array.append(rounded_num)
    return rounded_array