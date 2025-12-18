"""
QUESTION:
Create a function `originalDigits(s: str) -> str` that takes a string `s` as input and returns the digits in ascending order as a string and their counts as a dictionary. The input string `s` contains an out-of-order English representation of digits `0-9`. Each character in `s` is one of the characters `[e, g, f, i, h, o, n, s, r, u, t, w, v, x, z]`. The string `s` is guaranteed to be valid. The length of `s` is between 1 and 10^5.
"""

def originalDigits(s: str) -> str:
    from collections import Counter
    count = Counter(s)
    res = {}

    # looking for numbers which letters count unique in all digits
    res[0] = count['z']  # only digit with 'z' is '0'
    res[2] = count['w']  # only digit with 'w' is '2'
    res[4] = count['u']  # only digit with 'u' is '4'
    res[6] = count['x']  # only digit with 'x' is '6'
    res[8] = count['g']  # only digit with 'g' is '8'

    # there are other letters unique to other numbers but are also part of numbers we've counted
    res[3] = count['h'] - res[8]  # letter 'h' in '3' will be not present in '8'
    res[5] = count['f'] - res[4]  # letter 'f' in '5' will be not present in '4'
    res[7] = count['v'] - res[5]  # letter 'v' in '7' will not be present in '5'
    res[1] = count['o'] - res[0] - res[2] - res[4]  # letter 'o' is present in '0', '2' & '4'
    res[9] = count['i'] - res[5] - res[6] - res[8]  # letter 'i' is present in '5', '6' & '8'

    # creating the string representation of result
    result = [str(i) * num for i, num in sorted(res.items())] 

    return "".join(result)