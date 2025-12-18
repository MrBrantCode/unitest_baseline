"""
QUESTION:
Create a function called `rearrange_array` that takes two parameters: an array of integers and an integer 'n'. The function should rearrange the array's elements in a cyclical fashion according to 'n', where each element is shifted 'n' positions to the right, wrapping around to the beginning of the array if necessary. The function must handle large inputs efficiently.
"""

def rearrange_array(input_arr, n):
    length = len(input_arr)
    output_arr = [0] * length
    for i in range(length):
        new_index = (i + n) % length
        output_arr[new_index] = input_arr[i]
    return output_arr