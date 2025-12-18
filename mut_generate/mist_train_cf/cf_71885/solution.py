"""
QUESTION:
Implement the `maximumBinaryString` function, which takes a binary string `binary` as input and returns the maximum binary string that can be achieved after performing any number of operations. The allowed operations are substituting `"00"` with `"10"` and `"10"` with `"01"`. The binary string `x` is considered greater than binary string `y` if the decimal representation of `x` is greater than that of `y`. The length of `binary` is between 1 and 10^5 (inclusive) and `binary` is composed solely of `'0'`s and `'1'`s.
"""

def maximumBinaryString(binary: str) -> str:
    pre, zeros, n = 0, 0, len(binary)
    for i in range(n):
        if binary[i] == '0':
            zeros += 1
        else:
            if zeros == 0:
                pre += 1
    if zeros <= 1:
        return binary
    else:
        return '1' * pre + '1' * (zeros - 1) + '0' + '1' * (n - pre - zeros)