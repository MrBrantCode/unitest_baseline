"""
QUESTION:
Write a function named `hex_to_dec` that takes a 2D list `matrix_data` of hexadecimal strings as input. The function should convert the hexadecimal values to decimal and return a tuple containing the transformed 2D list of decimal values and a list of invalid hexadecimal entries. The function should handle invalid hexadecimal values by catching the `ValueError` exception and adding the invalid entries to the list. The input `matrix_data` may contain any number of sublists, and each sublist may contain any number of hexadecimal strings. The hexadecimal strings are prefixed with '0x'.
"""

def hex_to_dec(matrix_data):
    dec_matrix = []
    invalid_entries = []
    for sub_list in matrix_data:
        sub_dec_list = []
        for hex_val in sub_list:
            try:
                dec_val = int(hex_val, 16)
                sub_dec_list.append(dec_val)
            except ValueError:
                invalid_entries.append(hex_val)
        dec_matrix.append(sub_dec_list)
    return dec_matrix, invalid_entries