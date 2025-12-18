"""
QUESTION:
Create a function named `compute_checksum` that takes a list of hexadecimal numbers representing a data packet. The function should calculate the checksum of the data packet by iteratively adding each byte to the checksum and subtracting 0xFF if the checksum overflows beyond a single byte. The function then returns the complement of the checksum. 

Restrictions: The time complexity should be O(n), where n is the length of the data packet, and the space complexity should be O(1) to handle large data packets efficiently.
"""

def compute_checksum(data_packet):
    """
    Compute the checksum of a data packet and return its complement.

    The checksum is calculated by iteratively adding each byte to the checksum 
    and subtracting 0xFF if the checksum overflows beyond a single byte. The 
    function then returns the complement of the checksum.

    Args:
    data_packet (list): A list of hexadecimal numbers representing a data packet.

    Returns:
    int: The complement of the checksum.

    Time complexity: O(n), where n is the length of the data packet.
    Space complexity: O(1) to handle large data packets efficiently.
    """
    checksum = 0

    for byte in data_packet:
        checksum += byte

        if checksum > 0xFF:
            checksum -= 0xFF

    checksum_complement = ~checksum & 0xFF
    return checksum_complement