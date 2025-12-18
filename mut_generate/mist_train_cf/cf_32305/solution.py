"""
QUESTION:
Implement a function `getUniqueVouchers` that takes a list of voucher strings as input and returns a new list containing only the unique vouchers in the same order as they appear in the input list. A voucher is considered unique if it does not appear more than once in the input list.
"""

from typing import List

def getUniqueVouchers(vouchers: List[str]) -> List[str]:
    unique_vouchers = []
    seen_vouchers = set()
    
    for voucher in vouchers:
        if voucher not in seen_vouchers:
            unique_vouchers.append(voucher)
            seen_vouchers.add(voucher)
    
    return unique_vouchers