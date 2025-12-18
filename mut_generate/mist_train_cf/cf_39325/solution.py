"""
QUESTION:
Implement the `check_properties(num)` function to check the divisibility properties of a given positive integer `num`. The function should return a boolean value indicating whether the following properties hold true:
- The integer formed by extracting a substring of length 3 starting at index 2 from `num` is divisible by 2.
- The integer formed by extracting a substring of length 3 starting at index 3 from `num` is divisible by 3.
- The integer formed by extracting a substring of length 3 starting at index 4 from `num` is divisible by 5.
- The integer formed by extracting a substring of length 3 starting at index 5 from `num` is divisible by 7.
- The integer formed by extracting a substring of length 3 starting at index 6 from `num` is divisible by 11.
- The integer formed by extracting a substring of length 3 starting at index 7 from `num` is divisible by 13.
- The integer formed by extracting a substring of length 3 starting at index 8 from `num` is divisible by 17.

Note that the `sub_string` function is already implemented to extract a substring of length `rng` from `num` starting at index `start`.
"""

def check_properties(num):
    p1 = int(str(num)[1:4]) % 2 == 0
    p2 = int(str(num)[2:5]) % 3 == 0
    p3 = int(str(num)[3:6]) % 5 == 0
    p4 = int(str(num)[4:7]) % 7 == 0
    p5 = int(str(num)[5:8]) % 11 == 0
    p6 = int(str(num)[6:9]) % 13 == 0
    p7 = int(str(num)[7:10]) % 17 == 0
    return all([p1, p2, p3, p4, p5, p6, p7])