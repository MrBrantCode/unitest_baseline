"""
QUESTION:
Create a function `generate_license_key` that generates a license key embedded with information such as license expiration date, MAC address, and software restrictions. The function should take the following parameters: `mac_address`, `expiration_date`, and `software_restrictions`. The generated license key should be unique and tamper-proof, and it should be possible to verify the information embedded in the license key at a later time.
"""

import hashlib
import hmac
import base64

def generate_license_key(mac_address, expiration_date, software_restrictions):
    """
    Generates a unique license key embedded with information such as license expiration date, 
    MAC address, and software restrictions.

    Args:
    mac_address (str): The MAC address of the machine.
    expiration_date (str): The expiration date of the license.
    software_restrictions (str): The software restrictions.

    Returns:
    str: A unique license key.
    """

    # Combine the information into a single string
    info_string = mac_address + expiration_date + software_restrictions

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the info string
    hash_object.update(info_string.encode('utf-8'))

    # Get the digest of the hash object
    digest = hash_object.digest()

    # Use the HMAC algorithm to generate a unique license key
    license_key = hmac.new(digest, digest, hashlib.sha256).digest()

    # Encode the license key in base64 for easier storage and transmission
    encoded_license_key = base64.b64encode(license_key)

    # Return the encoded license key as a string
    return encoded_license_key.decode('utf-8')