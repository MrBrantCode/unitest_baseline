"""
QUESTION:
Create a function named `binary_to_hex` that takes an array of binary numbers as strings, converts each binary number into its equivalent hexadecimal number without using any in-built or third-party libraries or methods for binary to hex conversion, and returns an array of hexadecimal numbers. The function should ignore leading zeros in the hexadecimal numbers.
"""

def binary_to_hex(binary_array):
    def bin_to_dec(binary):
        decimal, i = 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal

    def dec_to_hex(n):
        hex_map = "0123456789ABCDEF"
        hex_num = ""
        while n != 0:
            r = n % 16
            hex_num = hex_map[r] + hex_num
            n = n // 16
        return hex_num

    hex_array = []
    for binary in binary_array:
        decimal = bin_to_dec(int(binary))
        hex_num = dec_to_hex(decimal)
        hex_array.append(hex_num)

    return hex_array