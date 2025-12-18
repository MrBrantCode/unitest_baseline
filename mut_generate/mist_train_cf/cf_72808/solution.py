"""
QUESTION:
Implement a function `organize_nums(num_list)` that takes a list of string representations of numerical values as input, transforms hexadecimal and binary numbers to decimal notation, and returns the list in ascending numerical order without using built-in sorting or transformation functions. The input list may include positive and negative integers, floating-point numbers, and numbers in scientific notation.
"""

def organize_nums(num_list):
    def hex_to_decimal(hex_val):
        hex_val = hex_val.lstrip("0x")
        dec_val = 0
        hex_digits = "0123456789abcdef"
        exp = len(hex_val) - 1
        for digit in hex_val:
            dec_val += hex_digits.index(digit.lower()) * (16 ** exp)
            exp -= 1
        return dec_val

    def bin_to_decimal(bin_val):
        bin_val = bin_val.lstrip("0b")
        dec_val = 0
        exp = len(bin_val) - 1
        for digit in bin_val:
            dec_val += int(digit) * (2 ** exp)
            exp -= 1
        return dec_val

    for i in range(len(num_list)):
        if num_list[i].startswith("0x"):
            num_list[i] = hex_to_decimal(num_list[i])
        elif num_list[i].startswith("0b"):
            num_list[i] = bin_to_decimal(num_list[i])
        else:
            num_list[i] = float(num_list[i])

    for i in range(len(num_list)):
        min_idx = i
        for j in range(i+1, len(num_list)):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    return num_list