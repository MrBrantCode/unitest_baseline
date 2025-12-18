"""
QUESTION:
Implement the function `parse_flags(flags: int) -> List[str]` that takes an integer `flags` as input and returns a list of strings representing the descriptions of the flags that are set. 

The flags and their corresponding descriptions are:
- `IPV4MAP` (1 << 0): "IPv4 Mapping"
- `IPV6MAP` (1 << 1): "IPv6 Mapping"
- `BLACKLISTFILE` (1 << 2): "Blacklist File"
- `TREEDATA` (1 << 2): "Tree Data"
- `STRINGDATA` (1 << 3): "String Data"
- `SMALLINTDATA` (1 << 4): "Small Integer Data"
- `INTDATA` (1 << 5): "Integer Data"
- `FLOATDATA` (1 << 6): "Float Data"
- `BINARYDATA` (1 << 7): "Binary Data"
- `ISPROXY` (1 << 0): "Is Proxy"
- `ISVPN` (1 << 1): "Is VPN"

Note that there are duplicate flag values, so you will need to handle this situation.
"""

from typing import List

def entrance(flags: int) -> List[str]:
    flag_descriptions = {
        1 << 0: ["IPv4 Mapping", "Is Proxy"],
        1 << 1: ["IPv6 Mapping", "Is VPN"],
        1 << 2: ["Blacklist File", "Tree Data"],
        1 << 3: "String Data",
        1 << 4: "Small Integer Data",
        1 << 5: "Integer Data",
        1 << 6: "Float Data",
        1 << 7: "Binary Data"
    }

    result = []
    for flag, description in flag_descriptions.items():
        if flags & flag:
            if isinstance(description, list):
                result.extend(description)
            else:
                result.append(description)
    return result