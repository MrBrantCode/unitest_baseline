"""
QUESTION:
You need to handle two extraordinarily large integers. The good news is that you don't need to perform any arithmetic operation on them. You just need to compare them and see whether they are equal or one is greater than the other.

Given two strings x and y, print either "x< y"(ignore space, editor issues), "x>y" or "x=y" depending on the values represented by x and y. x and y each consist of a decimal integer followed zero or more '!' characters. Each '!' represents the factorial operation. For example, "3!!" represents 3!! = 6! = 720.

Input - First line of input contains no. of testcases and each test consist of 2 lines x and y.

Ouptut - Print the required output.

SAMPLE INPUT
3
0!
1
9!!
999999999
456!!!
123!!!!!!

SAMPLE OUTPUT
x=y
x>y
x<y
"""

def compare_large_integers(x: str, y: str) -> str:
    def count_exclamations(s: str) -> int:
        cnt = 0
        i = len(s) - 1
        while i >= 0 and s[i] == '!':
            i -= 1
            cnt += 1
        return cnt

    cnt1 = count_exclamations(x)
    cnt2 = count_exclamations(y)

    swapped = 0
    if cnt2 < cnt1:
        cnt2, cnt1 = cnt1, cnt2
        x, y = y, x
        swapped = 1

    x = x[:len(x) - cnt1]
    y = y[:len(y) - cnt2]

    x = int(x)
    y = int(y)

    if x == 0:
        if cnt1 > 0:
            x = 1
            cnt1 -= 1
    if y == 0:
        if cnt2 > 0:
            cnt2 -= 1
            y = 1

    flag1 = cnt1
    flag2 = cnt2
    cnt2 = cnt2 - cnt1
    cnt1 = 0

    val = y

    while cnt2 > 0 and val <= x:
        b = val - 1
        while b > 0 and val <= x:
            val = val * b
            b -= 1
        cnt2 -= 1

    if swapped == 1:
        x, val = val, x

    if val > x:
        return "x<y"
    elif val == x:
        return "x=y"
    else:
        return "x>y"