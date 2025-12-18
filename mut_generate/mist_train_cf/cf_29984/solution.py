"""
QUESTION:
Implement a function `count_octet_combinations(ip_addresses)` that takes a list of valid IPv4 addresses as strings, where each address contains four octets separated by dots, and returns a dictionary where the keys are unique octet combinations (from one to four octets) and the values are the count of occurrences of each combination across all the IP addresses.
"""

def count_octet_combinations(ip_addresses):
    octet_count = {}
    for ip in ip_addresses:
        octets = ip.split('.')
        for i in range(4):
            octet_combination = '.'.join(octets[:i+1])
            if octet_combination in octet_count:
                octet_count[octet_combination] += 1
            else:
                octet_count[octet_combination] = 1
    return octet_count