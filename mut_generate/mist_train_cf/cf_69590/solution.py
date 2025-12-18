"""
QUESTION:
Create a function `classify_ip(ip)` that takes a string representing an IP address as input and returns its classification into one of the following categories: Class A, Class B, Class C, Class D (Multicast), or Class E (Reserved). The function should first validate the IP address using a regular expression to ensure it follows the standard IPV4 format (four sets of numbers ranging from 0-255 separated by periods). The classification is based on the first octet of the IP address.
"""

import re

def classify_ip(ip):
    regex_ip_format = r'\b((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\b'
    if re.fullmatch(regex_ip_format, ip):
        first_octet = int(ip.split('.')[0])
        if 1 <= first_octet <= 126:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 254:
            return "Class E (Reserved)"
    else:
        return "Invalid IP"