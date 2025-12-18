"""
QUESTION:
Write a function `calculate_array` that takes an initial array of 5 elements and returns a new array of 10 elements based on specific calculations. 

The first 5 elements of the output array should follow these rules: 
- the first element is the sum of the first and second element of the previous array, 
- the second element is the difference between the first and second element of the previous array, 
- the third element is the product of the first and second element of the previous array, 
- the fourth element is the quotient of the first and second element of the previous array, 
- the fifth element is the remainder of the division between the first and second element of the previous array.

For the remaining elements (6th to 10th), the rules are:
- the sixth element is the sum of the third and fourth element of the previous array,
- the seventh element is the difference between the third and fourth element of the previous array,
- the eighth element is the product of the third and fourth element of the previous array,
- the ninth element is the quotient of the third and fourth element of the previous array,
- the tenth element is the remainder of the division between the third and fourth element of the previous array.
"""

def calculate_array(arr):
    """
    This function takes an initial array of 5 elements and returns a new array of 10 elements based on specific calculations.

    :param arr: The initial array of 5 elements
    :return: A new array of 10 elements
    """
    result = [
        arr[0] + arr[1],  # sum of the first and second element
        arr[0] - arr[1],  # difference between the first and second element
        arr[0] * arr[1],  # product of the first and second element
        arr[0] / arr[1] if arr[1] != 0 else 0,  # quotient of the first and second element
        arr[0] % arr[1] if arr[1] != 0 else 0,  # remainder of the division between the first and second element
        arr[2] + arr[3],  # sum of the third and fourth element
        arr[2] - arr[3],  # difference between the third and fourth element
        arr[2] * arr[3],  # product of the third and fourth element
        arr[2] / arr[3] if arr[3] != 0 else 0,  # quotient of the third and fourth element
        arr[2] % arr[3] if arr[3] != 0 else 0  # remainder of the division between the third and fourth element
    ]
    return result