"""
QUESTION:
Create a function called `sort_numeric_strings` that takes an array of stringified numerical values as input, including positive and negative integers, real numbers, numbers in scientific notation, hexadecimal notation, and binary notation. The function should convert hexadecimal and binary numbers to decimal notation, then sort the array in ascending numerical order using a custom sorting algorithm (without using Python's built-in sort function). The function should also avoid using built-in functions for converting hexadecimal and binary numbers to decimal.
"""

def sort_numeric_strings(array):
    def hex_to_decimal(hex_string):
        hex_string = hex_string[2:]
        hex_base = 16
        decimal_num = 0
        for i in range(len(hex_string)):
            decimal_num += int(hex_string[i], 16) * (hex_base ** (len(hex_string) - 1 - i))
        return decimal_num

    def bin_to_decimal(bin_string):
        bin_string = bin_string[2:]
        bin_base = 2
        decimal_num = 0
        for i in range(len(bin_string)):
            decimal_num += int(bin_string[i]) * (bin_base ** (len(bin_string) - 1 - i))
        return decimal_num

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    decimal_array = []
    for string in array:
        if string.startswith('0x'):
            decimal_array.append(hex_to_decimal(string))
        elif string.startswith('0b'):
            decimal_array.append(bin_to_decimal(string))
        elif 'e' in string:
            decimal_array.append(float(string))
        else:
            decimal_array.append(float(string))
    return bubble_sort(decimal_array)