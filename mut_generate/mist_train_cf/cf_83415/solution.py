"""
QUESTION:
Write three functions, `toHex(num)`, `toOct(num)`, and `toBin(num)`, that take a 32-bit signed integer `num` as input and return its hexadecimal, octal, and binary representations as strings, respectively. The hexadecimal representation should be in lowercase and should not contain extra leading zeros. The binary and octal representations should also not contain extra leading zeros. If `num` is negative, use two's complement representation. You must not use any library methods that directly convert or format numbers to hexadecimal, binary, or octal.
"""

def toHex(num: int) -> str:
    if num == 0: 
        return '0'
    mp = '0123456789abcdef'  
    ans = ''
    for _ in range(8):
        n = num & 15       
        c = mp[n]          
        ans = c + ans
        num = num >> 4
    return ans.lstrip('0')  

def toOct(num: int) -> str:
    if num == 0: 
        return '0'
    mp = '01234567'  
    ans = ''
    for _ in range(11):
        n = num & 7       
        c = mp[n]          
        ans = c + ans
        num = num >> 3
    return ans.lstrip('0')  

def toBin(num: int) -> str:
    if num == 0: 
        return '0'
    mp = '01'  
    ans = ''
    for _ in range(32):
        n = num & 1       
        c = mp[n]          
        ans = c + ans
        num = num >> 1
    return ans.lstrip('0')  