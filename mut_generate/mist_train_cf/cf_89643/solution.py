"""
QUESTION:
Create a method `find_valid_ip_addresses` that takes two parameters: `string` and `subnet_mask`. The `string` should be a 11-digit string containing only digits (0-9) where the first 9 digits are always "192168111" and the last 2 digits represent the host portion of the IP address. The `subnet_mask` is a string of 32 bits (0s and 1s) that determines the network portion and host portion of the IP address.

The method should return a list of all valid IP addresses that can be formed in the standard dot-decimal notation (e.g. "192.168.111.0"). The host portion of the IP address should be between 0 and 4. Leading zeroes are not allowed in any part of the IP address.
"""

def find_valid_ip_addresses(string, subnet_mask):
    # Create a list to store the valid IP addresses
    valid_ip_addresses = []
    
    # Check if the string length is valid
    if len(string) != 11:
        return valid_ip_addresses
    
    # Check if the subnet mask length is valid
    if len(subnet_mask) != 32:
        return valid_ip_addresses
    
    # Check if the network portion of the IP address is valid
    if string[:9] != "192168111":
        return valid_ip_addresses
    
    # Get the host portion of the IP address
    host_portion = string[9:]
    
    # Check if the host portion is valid
    if not host_portion.isdigit() or int(host_portion) > 4:
        return valid_ip_addresses
    
    # Convert the subnet mask to a list of 4 octets
    subnet_mask_octets = [subnet_mask[i:i+8] for i in range(0, 32, 8)]
    
    # Convert the host portion to binary
    host_binary = "{0:04b}".format(int(host_portion))
    
    # Iterate through all possible combinations of the subnet mask and host portion
    for i in range(16):
        # Convert the current index to binary
        index_binary = "{0:04b}".format(i)
        
        # Create a new IP address by combining the network portion, the index, and the host portion
        ip_address = "192.168.111." + index_binary + host_binary
        
        # Check if the IP address is valid based on the subnet mask
        if all(subnet_bit == "1" for subnet_bit in subnet_mask_octets[i]):
            valid_ip_addresses.append(ip_address)
    
    return valid_ip_addresses