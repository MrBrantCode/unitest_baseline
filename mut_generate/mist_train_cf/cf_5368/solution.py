"""
QUESTION:
Write a function named `format_and_validate_ip` that takes a list of IP addresses and a subnet prefix length as input, formats each IP address with its corresponding network address and subnet mask in CIDR notation, validates the IP addresses to ensure they are valid and within the range of private IP addresses, and calculates the number of possible host addresses within each network. The function should not use any built-in libraries or functions for IP address manipulation or validation, and should include error handling for invalid IP addresses.
"""

def format_and_validate_ip(ip_list, subnet_prefix_length):
    def validate_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or int(part) > 255:
                return False
        return True

    def validate_private_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        if parts[0] != '10' and parts[0] != '172' and parts[0] != '192':
            return False
        if parts[0] == '10' or (parts[0] == '172' and 16 <= int(parts[1]) <= 31) or (parts[0] == '192' and parts[1] == '168'):
            return True
        return False

    def format_ip(ip):
        parts = ip.split('.')
        network = '.'.join(parts[:3]) + '.0'
        subnet = str(len(bin(int(parts[3]))[2:]))
        return f'{ip}/{subnet}'

    def calculate_host_addresses(subnet):
        return 2 ** (32 - subnet) - 2

    for ip in ip_list:
        if validate_ip(ip) and validate_private_ip(ip):
            network = format_ip(ip)
            host_addresses = calculate_host_addresses(subnet_prefix_length)
            print(f'{ip} - Network: {network} - Subnet Mask: {subnet_prefix_length} - Host Addresses: {host_addresses}')
        else:
            print('Invalid IP address or not a private IP')