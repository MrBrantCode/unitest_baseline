"""
QUESTION:
Extract the version number from a given filename, where the version number is denoted by a lowercase 'v' followed by a sequence of digits. Implement the function `get_version_number(filename: str) -> Optional[str]` that takes a filename as input and returns the extracted version number. If the filename is empty or does not contain a valid version number, return None.
"""

from typing import Optional

def get_version_number(filename: str) -> Optional[str]:
    if filename:
        tx_list = filename.split('_') 
        tx_list.reverse() 
        for tx in tx_list:
            if tx.startswith('v') and tx[1:].isdigit():  
                return tx[1:]  
    return None 