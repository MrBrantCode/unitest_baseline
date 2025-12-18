"""
QUESTION:
Write a function `compute_checksum` that takes a list of hexadecimal numbers representing a data packet and returns the complement of the checksum. The checksum is calculated as the sum of all bytes in the data packet. The checksum and its complement should be within the range 0-255.
"""

def compute_checksum(data_packet):
    checksum = 0
    for byte in data_packet:
        checksum += byte
    checksum = checksum & 0xff  
    return ~checksum & 0xff 