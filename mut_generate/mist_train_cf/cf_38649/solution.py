"""
QUESTION:
Create a function called `protocol_type` that takes two arguments: `address_family` and `protocol_number`, both integers representing the address family and protocol number, respectively. The function should return a string representing the protocol type based on the given address family and protocol number. The function should map address family and protocol number to protocol type as follows: 
- If `address_family` is AF_INET (2) and `protocol_number` is IPPROTO_IP (0), return "IPv4".
- If `address_family` is AF_INET6 (10) and `protocol_number` is IPPROTO_IP (0), return "IPv6".
- For any other combination of `address_family` and `protocol_number`, return "Unknown".
"""

def protocol_type(address_family, protocol_number):
    if address_family == 2 and protocol_number == 0:
        return "IPv4"
    elif address_family == 10 and protocol_number == 0:
        return "IPv6"
    else:
        return "Unknown"