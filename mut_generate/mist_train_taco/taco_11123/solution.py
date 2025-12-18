"""
QUESTION:
Define two functions: `hex_to_bin` and `bin_to_hex` (or `hexToBin` and `binToHex`)


# hex_to_bin

Takes a hexadecimal string as an argument .

**Note:** This string can contain upper or lower case characters and start with any amount of zeros.

Returns the binary representation (without leading zeros) of the numerical value of the hexadecimal string.

Examples:

```
"00F"    -->  "1111"
"5"      -->  "101"
"00000"  -->  "0"
"04D2"   -->  "10011010010"
```

# bin_to_hex

Takes a binary string (with or without leading zeros) as an argument .

Returns the hexadecimal representation of the numerical value of the binary string.

**Note:** Any non-numerical characters should be lower case


Examples:

```
"1111"         -->  "f"
"000101"       -->  "5"
"10011010010"  -->  "4d2"
```

**Note:** You can assume all arguments are valid so there is no need for error checking.

Oh, and I've disabled a few things.


Any feedback would be much appreciated
"""

bin2hex = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', 
    '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
    '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', 
    '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'
}
hex2bin = {v: k for (k, v) in bin2hex.items()}

def hex_to_bin(hex_str: str) -> str:
    res = ''
    while hex_str:
        res += hex2bin[hex_str[0].lower()]
        hex_str = hex_str[1:]
    return res.lstrip('0') or '0'

def bin_to_hex(bin_str: str) -> str:
    res = ''
    bin_str = '0' * (4 - len(bin_str) % 4) + bin_str
    while bin_str:
        res += bin2hex[bin_str[:4]]
        bin_str = bin_str[4:]
    return res.lstrip('0') or '0'