"""
QUESTION:
Create a method named `find_valid_ip_addresses` that takes two parameters: a string of digits and a 32-bit subnet mask string of 0s and 1s. The method should return a list of all valid IP addresses in standard dot-decimal notation that can be formed using the given string, considering the subnet mask restrictions.
"""

def find_valid_ip_addresses(string, subnet_mask):
    valid_ips = []
    
    # Iterate through all possible combinations of network portion and host portion
    for i in range(0, len(string)):
        network_portion = string[:i+1]
        host_portion = string[i+1:]
        
        # Check if the network portion and host portion are valid according to the subnet mask
        if len(network_portion) <= len(subnet_mask) and all(network_portion[j] == subnet_mask[j] for j in range(len(network_portion))):
            if len(host_portion) <= 3 and int(host_portion) <= 255:
                ip_address = network_portion + "." + host_portion
                valid_ips.append(ip_address)
    
    return valid_ips