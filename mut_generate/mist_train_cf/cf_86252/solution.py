"""
QUESTION:
Write a function `compute_checksum(data_packet)` that calculates the checksum of a given data packet and returns the complement of the checksum. The data packet is a list of hexadecimal numbers. The checksum is calculated by summing all the bytes in the data packet, subtracting 0xFF from the sum whenever it overflows beyond the range of a single byte, and then taking the complement of the sum. The function should have a time complexity of O(n), where n is the length of the data packet, and a space complexity of O(1).
"""

def compute_checksum(data_packet):
    checksum = 0

    for byte in data_packet:
        checksum += byte

        if checksum > 0xFF:
            checksum -= 0xFF

    checksum_complement = ~checksum & 0xFF
    return checksum_complement