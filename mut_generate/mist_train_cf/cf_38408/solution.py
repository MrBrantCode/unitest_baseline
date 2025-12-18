"""
QUESTION:
Implement a function named `build_packet` that takes two parameters: `data` (raw DNS data in bytes format) and `ip_address` (a string representing an IP address). The function should construct a DNS packet with the appropriate format by modifying the raw DNS data and appending the IP address. The DNS packet format should include a 12-byte DNS header followed by the DNS question section, and the DNS header should be modified to set the answer resource records to 1. The function should return the constructed DNS packet in bytes format. The constructed packet should be able to pass a unit test where the input is `b"^4\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01"` and the IP address is `"192.168.0.1"`, and the expected output is `b"^4\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04\xc0\xa8\x00\x01"`.
"""

def build_packet(data, ip_address):
    # Modify the DNS header to set the answer resource records to 1
    modified_header = data[:2] + b'\x81\x80' + data[4:]
    
    # Append the IP address to the modified DNS data
    ip_address_bytes = ip_address.split('.')
    ip_address_bytes = [int(byte) for byte in ip_address_bytes]
    ip_address_bytes = bytes(ip_address_bytes)
    constructed_packet = modified_header + b'\xc0\x0c\x00\x01\x00\x01\x00\x00\x00<\x00\x04' + ip_address_bytes
    
    return constructed_packet