"""
QUESTION:
Write a function `validateMacAndInterface` that takes a string `MAC` as input and returns `"Ethernet"` if `MAC` is a valid MAC address with a valid Ethernet interface name, `"Wireless"` if `MAC` is a valid MAC address with a valid wireless interface name, or `"Neither"` otherwise. A valid MAC address is in the form `"xx:xx:xx:xx:xx:xx/interface"` where `xx` is a hexadecimal string and the interface name starts with either "eth" for Ethernet interfaces or "wlan" for wireless interfaces, followed by a number.
"""

import re

def validateMacAndInterface(MAC: str) -> str:
    validMac = re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"
        + "(?P<interface>/eth[0-9]+|/wlan[0-9]+)$", MAC)
    if validMac:
        interface = validMac.group("interface")
        if interface.startswith("/eth"):
            return "Ethernet"
        elif interface.startswith("/wlan"):
            return "Wireless"
    return "Neither"