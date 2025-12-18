"""
QUESTION:
Create a function named `is_valid_ip` that takes a string `ip_str` as input and returns `True` if it's a valid IP address and `False` otherwise. The function should check if the string consists of exactly four segments separated by periods, and each segment is a digit within the range of 0 to 255.
"""

def is_valid_ip(ip_str):
    ip_segments = ip_str.split('.')
    if len(ip_segments) != 4:
        return False
    for seg in ip_segments:
        if not seg.isdigit():
            return False
        seg_num = int(seg)
        if seg_num < 0 or seg_num > 255 or (seg_num != 0 and seg[0] == '0'):
            return False
    return True