"""
QUESTION:
Write a function named `max_value` that takes a 2D list `matrix` and returns the maximum value between the maximum values of the third and fourth rows. The matrix is a 4x4 2D list of integers, and the function should use helper function `max_num` to compare two numbers and return the larger one, and function `max_array` to find the maximum value in a 1D list. 

The function `max_num` should take two integers `num1` and `num2` as input, and return `num1` if `num1` is greater than or equal to `num2`, otherwise return `num2`. The function `max_array` should take a 1D list `arr` as input, and return the maximum value in the list.
"""

def max_value(matrix):
    def max_num(num1, num2):
        if num1 >= num2:
          return num1
        else:
          return num2

    def max_array(arr):
        max_val = arr[0]
        for num in arr:
            max_val = max_num(max_val, num)
        return max_val

    return max_num(max_array(matrix[2]), max_array(matrix[3]))