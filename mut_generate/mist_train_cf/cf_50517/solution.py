"""
QUESTION:
Write a function called `remove_leading_zeros(ip)` that takes a string representing an IP address as input and returns the IP address with leading zeroes removed from each part. The function should also validate the IP address and return an error message if it is invalid. An IP address is considered valid if it contains exactly four parts separated by dots, and each part is an integer between 0 and 255.
"""

def remove_leading_zeros(ip):
  # Splitting the ip address
  parts = ip.split(".")
  
  # Check if ip address is valid
  if len(parts)!=4:
    return 'Error: Invalid IP address'

  stripped_ip = []
  for i in parts:
    try:
        num = int(i)
    except ValueError:
        return 'Error: Invalid IP address'
    if num<0 or num>255:
        return 'Error: Invalid IP address'
    stripped_ip.append(str(num))
  
  return ".".join(stripped_ip)