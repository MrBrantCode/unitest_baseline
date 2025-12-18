"""
QUESTION:
Compute the complement of the checksum of a given data packet represented as a list of hexadecimal numbers, where the checksum is calculated by adding each byte to the total sum, handling overflow beyond a single byte by subtracting 0xFF, and then taking the complement of the result. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the data packet.
"""

def compute_checksum(data_packet):
    checksum = 0
    for byte in data_packet:
        checksum += byte
        if checksum > 0xFF:
            checksum -= 0xFF
    return ~checksum & 0xFF