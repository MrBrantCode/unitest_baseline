"""
QUESTION:
Implement a function named "validate_params(ip, netmask, gateway)" in Python that takes three string parameters representing an IP address, a subnet mask, and a default gateway. The function should validate these network parameters for their correct format and return "Valid parameters" if all are valid, or an error message indicating which parameter is invalid. The function should handle cases where the IP address, subnet mask, or default gateway is invalid.
"""

import ipaddress

def validate_params(ip, netmask, gateway):
  # validate IP address
  try:
    ipaddress.IPv4Address(ip)
  except ipaddress.AddressValueError:
    return "Invalid IP address"

  # validate netmask
  try:
    ipaddress.IPv4Address(netmask)
  except ipaddress.AddressValueError:
    return "Invalid netmask"

  # validate gateway
  try:
    ipaddress.IPv4Address(gateway)
  except ipaddress.AddressValueError:
    return "Invalid gateway"
  
  # if no exceptions encountered
  return "Valid parameters"