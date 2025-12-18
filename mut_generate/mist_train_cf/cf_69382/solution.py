"""
QUESTION:
Create a function `validIPAddress` that takes a string `IP` as input and returns `"IPv4"` if `IP` is a valid IPv4 address with a valid subnet mask, `"IPv6"` if `IP` is a valid IPv6 address with a valid subnet mask, or `"Neither"` if `IP` is not a correct IP of any type or the subnet mask is invalid.

The input string `IP` consists only of English letters, digits, and the characters `'.'`, `':'`, and `'/'`. A valid IPv4 address has the form `x1.x2.x3.x4/mask` where `0 <= xi <= 255`, `xi` cannot contain leading zeros, and `0 <= mask <= 32`. A valid IPv6 address has the form `x1:x2:x3:x4:x5:x6:x7:x8/mask` where `1 <= xi.length <= 4`, `xi` is a hexadecimal string, and `0 <= mask <= 128`.
"""

import ipaddress

def validIPAddress(IP: str) -> str:
    if '/' in IP:
        subnetIndex = IP.find('/')
        subnet = int(IP[subnetIndex + 1:])
        ip = IP[:subnetIndex]
    else:
        return "Neither"
        
    if ':' in IP:
        if subnet > 128:
            return "Neither"
        else:
            try:
                ipaddress.IPv6Address(ip)
                return "IPv6"
            except ValueError:
                return "Neither"
    elif '.' in IP:
        if subnet > 32:
            return "Neither"
        else:
            try:
                ipaddress.IPv4Address(ip)
                return "IPv4"
            except ValueError:
                return "Neither"
    else:
        return "Neither"