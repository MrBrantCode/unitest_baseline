"""
QUESTION:
A checksum is an algorithm that scans a packet of data and returns a single number. The idea is that if the packet is changed, the checksum will also change, so checksums are often used for detecting
transmission errors, validating document contents, and in many other situations where it is necessary to detect undesirable changes in data.

For this problem, you will implement a checksum algorithm called Quicksum. A Quicksum packet allows only uppercase letters and spaces. It always begins and ends with an uppercase letter. 

Otherwise, spaces and uppercase letters can occur in any combination, including consecutive spaces.

A Quicksum is the sum of the products of each character’s position in the packet times the character’s value. A space has a value of zero, while letters have a value equal to their position in the alphabet. 

So, ```A = 1```, ```B = 2```, etc., through ```Z = 26```. Here are example Quicksum calculations for the packets “ACM” and “A C M”:
 
  ACM
1 × 1 + 2 × 3 + 3 × 13 = 46 

A C M
1 x 1 + 3 x 3 + 5 * 13 = 75


When the packet doesn't have only uppercase letters and spaces or just spaces the result to quicksum have to be zero (0).
 
  AbqTH #5 = 0
"""

from string import ascii_uppercase

def calculate_quicksum(packet: str) -> int:
    """
    Calculate the Quicksum of a given packet of data.

    The Quicksum is calculated by summing the products of each character's position 
    in the packet times the character's value. A space has a value of zero, while 
    letters have a value equal to their position in the alphabet (A=1, B=2, ..., Z=26).

    If the packet contains any invalid characters (non-uppercase letters or non-spaces), 
    the function returns 0.

    Args:
        packet (str): The packet of data to be processed.

    Returns:
        int: The Quicksum of the packet, or 0 if the packet contains invalid characters.
    """
    values = {x: i for (i, x) in enumerate(ascii_uppercase, 1)}
    
    # Check if the packet contains only uppercase letters and spaces
    if not all(c.isspace() or c.isupper() for c in packet):
        return 0
    
    # Calculate the Quicksum
    return sum((values.get(c, 0) * i for (i, c) in enumerate(packet, 1)))