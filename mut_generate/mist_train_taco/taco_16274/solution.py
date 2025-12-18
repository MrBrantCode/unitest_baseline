"""
QUESTION:
You have number a, whose decimal representation quite luckily contains digits 1, 6, 8, 9. Rearrange the digits in its decimal representation so that the resulting number will be divisible by 7.

Number a doesn't contain any leading zeroes and contains digits 1, 6, 8, 9 (it also can contain another digits). The resulting number also mustn't contain any leading zeroes.


-----Input-----

The first line contains positive integer a in the decimal record. It is guaranteed that the record of number a contains digits: 1, 6, 8, 9. Number a doesn't contain any leading zeroes. The decimal representation of number a contains at least 4 and at most 10^6 characters.


-----Output-----

Print a number in the decimal notation without leading zeroes — the result of the permutation.

If it is impossible to rearrange the digits of the number a in the required manner, print 0.


-----Examples-----
Input
1689

Output
1869

Input
18906

Output
18690
"""

def rearrange_digits_divisible_by_7(a: str) -> str:
    l = len(a)
    book = [0] * 128
    a = list(a)
    
    for i in range(l):
        a[i] = chr(ord(a[i]) - ord('0'))
        book[ord(a[i])] += 1
    
    num = 0
    m = 0
    buf = []
    
    for i in range(1, 10):
        if i in (1, 8, 6, 9):
            for j in range(1, book[i]):
                buf.append(i)
                m = (10 * m + i) % 7
                num += 1
        else:
            for j in range(1, book[i] + 1):
                buf.append(i)
                m = (10 * m + i) % 7
                num += 1
    
    m = m * 10000 % 7
    mp = [9681, 1896, 9861, 1698, 6891, 6981, 6819]
    buf.append(mp[m])
    num += 4
    
    buf.append('0' * (l - num))
    
    return ''.join(map(str, buf))