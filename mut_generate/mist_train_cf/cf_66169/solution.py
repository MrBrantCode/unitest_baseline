"""
QUESTION:
Write a function named `categorize_mac` that takes a list of MAC addresses as input, validates them using a regex pattern, and categorizes them by manufacturer based on their first 3 bytes (Organizationally Unique Identifier or OUI). The function should be able to handle a large collection of MAC addresses and categorize them into 'Apple', 'Dell', and 'Other' manufacturers. Assume that the OUI prefixes for 'Apple' and 'Dell' manufacturers are '00:1C:B3', '00:1D:4F', '00:61:71' and '00:25:BC', 'E0:5F:B9', '04:0C:CE' respectively. The function should return a dictionary where keys are the manufacturer names and values are lists of corresponding MAC addresses.
"""

import re


def categorize_mac(mac_addresses):
    pattern = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    categorized_mac = {}

    for mac in mac_addresses:
        if re.fullmatch(pattern, mac):
            oui = mac[:8].upper().replace("-", ":")
            if oui in ['00:25:BC', 'E0:5F:B9', '04:0C:CE']:  # Dell OUIs
                categorized_mac.setdefault('Dell', []).append(mac)
            elif oui in ['00:1C:B3', '00:1D:4F', '00:61:71']:  # Apple OUIs
                categorized_mac.setdefault('Apple', []).append(mac)
            else:
                categorized_mac.setdefault('Other', []).append(mac)
    
    return categorized_mac