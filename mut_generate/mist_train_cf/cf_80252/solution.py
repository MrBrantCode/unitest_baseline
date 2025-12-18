"""
QUESTION:
Design a function `analyze_ipv6` that takes an IPv6 address as input and returns its binary representation, subnet mask, prefix length, and network address. The function should handle exceptions for invalid inputs, including invalid IPv6 addresses and netmasks. The function should support both global unicast and unique local addresses.
"""

import ipaddress

def analyze_ipv6(ipv6):
    try:
        # creates IPv6 object
        ip = ipaddress.IPv6Interface(ipv6)

        # binary representation of the address
        binary_repr = ''.join(format(int(x, 16), '016b') for x in ip.ip.exploded.split(':'))

        # Subnet mask, Prefix Length and Network Address
        subnet_mask = ip.network.with_netmask.split('/')[1]
        prefix_length = ip.network.prefixlen
        network_address = ip.network.network_address

        return {"IPv6": str(ip),
                "Binary Representation": str(binary_repr),
                "Subnet Mask": str(subnet_mask),
                "Prefix Length": str(prefix_length),
                "Network Address": str(network_address)}

    except ipaddress.AddressValueError:
        return 'The provided IP address is not a valid IPv6 address.'

    except ipaddress.NetmaskValueError:
        return 'The provided IP address has an invalid netmask.'