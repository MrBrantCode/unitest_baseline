"""
QUESTION:
The year 2015 is almost over.

Limak is a little polar bear. He has recently learnt about the binary system. He noticed that the passing year has exactly one zero in its representation in the binary system — 2015_10 = 11111011111_2. Note that he doesn't care about the number of zeros in the decimal representation.

Limak chose some interval of years. He is going to count all years from this interval that have exactly one zero in the binary representation. Can you do it faster?

Assume that all positive integers are always written without leading zeros.


-----Input-----

The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10^18) — the first year and the last year in Limak's interval respectively.


-----Output-----

Print one integer – the number of years Limak will count in his chosen interval.


-----Examples-----
Input
5 10

Output
2

Input
2015 2015

Output
1

Input
100 105

Output
0

Input
72057594000000000 72057595000000000

Output
26



-----Note-----

In the first sample Limak's interval contains numbers 5_10 = 101_2, 6_10 = 110_2, 7_10 = 111_2, 8_10 = 1000_2, 9_10 = 1001_2 and 10_10 = 1010_2. Two of them (101_2 and 110_2) have the described property.
"""

def count_years_with_one_zero_in_binary(a, b):
    count = 0
    for i in range(2, 61):
        num = (1 << i) - 1
        for j in range(0, i - 1):
            year = num - (1 << j)
            if a <= year <= b:
                count += 1
    return count