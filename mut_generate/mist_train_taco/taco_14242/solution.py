"""
QUESTION:
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).


Example 1:

Input:
3

Output:
3



Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

def find_nth_digit(n: int) -> int:
    i = count = 9
    while count < n:
        i *= 10
        count += i * len(str(i))
    div, mod = divmod(n - (count - i * len(str(i))), len(str(i)))
    target = i // 9 - 1 + div
    if mod == 0:
        return int(str(target)[-1])
    else:
        return int(str(target + 1)[mod - 1])