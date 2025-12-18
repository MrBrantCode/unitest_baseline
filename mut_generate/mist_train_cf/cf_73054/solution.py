"""
QUESTION:
Implement a function `originaldigits(s: str) -> str` that takes a string `s` containing the English word representations of digits from 0 to 9, and returns a string where each digit from 0 to 9 appears as many times as it appears in `s`. The string `s` is expected to contain the letters 'z', 'w', 'u', 'x', 'g', 'h', 'f', 'o', 'v', and 'i' which uniquely identify the digits 0, 2, 4, 6, 8, 3, 5, 1, 7, and 9 respectively. The output string should have the digits sorted in ascending order.
"""

def originaldigits(s: str) -> str:
    from collections import Counter
    count = Counter(s)
    res = dict()

    # looking for numbers which letters count unique in all digits
    res[0] = count['z']
    res[2] = count['w']
    res[4] = count['u']
    res[6] = count['x']
    res[8] = count['g']

    # there are other letters unique to other numbers but are also part of numbers we've counted
    res[3] = count['h'] - res[8]
    res[5] = count['f'] - res[4]
    res[7] = count['v'] - res[5]
    res[1] = count['o'] - res[0] - res[2] - res[4]
    res[9] = count['i'] - res[5] - res[6] - res[8]

    # creating the string representation of result
    result = [str(i) * num for i, num in sorted(res.items())] 

    return "".join(result)