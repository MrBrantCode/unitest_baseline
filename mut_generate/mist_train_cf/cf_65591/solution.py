"""
QUESTION:
Write a function named `determine_max_num` that takes the size of RAM in bytes as input and calculates the maximum number of 256-bit numbers that can fit in the given size of RAM. The function should handle potential memory overflow exceptions and provide the results. The input sizes of RAM are 1GB, 500MB, 1MB, and 256KB.
"""

def determine_max_num(storage_size_in_byte):
    '''The function to calculate the maximum number of 256-bits numbers that can fit in a given size of RAM'''
    bits_per_byte = 8 # 1 Byte = 8 Bit
    size_per_number_in_byte = 256 / bits_per_byte # Size of a 256-bit number in byte

    # Calculate the maximum number of 256-bit numbers that can fit in the given size RAM
    try:
        max_num = int(storage_size_in_byte / size_per_number_in_byte)
        return max_num
    except MemoryError:
        return None