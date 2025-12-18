"""
QUESTION:
Write a function `find_subnet_mask(ip)` that determines the subnet mask of a given IP address. The function should take an IP address as a string in the format "xxx.xxx.xxx.xxx" as input and return the corresponding subnet mask as a string. The function should assume a classful network design where the first octet of the IP address determines the subnet mask.
"""

def find_subnet_mask(ip):
  ip_parts = ip.split('.')
  first_octet = int(ip_parts[0])

  if (first_octet >= 1 and first_octet <= 126):
    return "255.0.0.0" # Class A
  elif (first_octet >= 128 and first_octet <= 191):
    return "255.255.0.0" # Class B
  elif (first_octet >= 192 and first_octet <= 223):
    return "255.255.255.0" # Class C
  elif (first_octet >= 224 and first_octet <= 239):
    return "Reserved for future use" # Class D
  else:
    return "Reserved for future use" # Class E