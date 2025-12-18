"""
QUESTION:
Create a function `sjis_to_euc` that takes a string encoded in Shift-JIS and returns the equivalent string encoded in EUC-JP. The function should handle the conversion correctly, ensuring the output string is encoded in EUC-JP.
"""

import codecs

def sjis_to_euc(input_string):
    sjis_bytes = input_string.encode('sjis')  
    euc_bytes = sjis_bytes.decode('euc_jp', 'ignore').encode('euc_jp')  
    return euc_bytes.decode('euc_jp')  