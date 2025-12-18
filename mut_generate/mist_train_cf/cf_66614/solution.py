"""
QUESTION:
Create a function named `float_dec2base(num, base)` that converts a given decimal number `num` to a given base `base` (between 2 and 16) up to three decimal places. The function should handle both integer and fractional parts of the number. The conversion should be precise for integer parts but may not be exact for fractional parts in bases that cannot exactly represent the decimal fraction.
"""

def float_dec2base(num, base):
    base_digs = "0123456789ABCDEF"
    if num < 0:
        return "-" + float_dec2base(-num, base)
    whole = int(num)
    frac = num - whole
    res = ""
    if whole == 0:
        res = "0"
    else:
        while whole != 0:
            res = base_digs[whole % base] + res
            whole = whole // base
    if frac != 0.0:
        res += '.'
        for i in range(3):  # up to three decimal places
            frac = frac * base
            digit = int(frac)
            frac -= digit
            res += base_digs[digit]
    return res