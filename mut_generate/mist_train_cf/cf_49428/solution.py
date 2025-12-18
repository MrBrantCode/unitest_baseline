"""
QUESTION:
Implement the function `compress_array` that takes a list of integers as input and returns a string representing the compressed array using Run-Length Encoding (RLE) compression technique. The function should handle empty input lists and arrays with no consecutive repeated integers.
"""

def compress_array(array):
    if not array:
        return ''
    else:
        result = ''
        count = 1
        for i in range(1, len(array)):
            if array[i] != array[i - 1]:
                result += str(array[i - 1]) + str(count)
                count = 1
            else:
                count += 1
        result += str(array[-1]) + str(count)
        return result