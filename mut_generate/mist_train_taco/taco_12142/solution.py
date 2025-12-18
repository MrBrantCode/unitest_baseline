"""
QUESTION:
You have number a, whose decimal representation quite luckily contains digits 1, 6, 8, 9. Rearrange the digits in its decimal representation so that the resulting number will be divisible by 7.

Number a doesn't contain any leading zeroes and contains digits 1, 6, 8, 9 (it also can contain another digits). The resulting number also mustn't contain any leading zeroes.

Input

The first line contains positive integer a in the decimal record. It is guaranteed that the record of number a contains digits: 1, 6, 8, 9. Number a doesn't contain any leading zeroes. The decimal representation of number a contains at least 4 and at most 106 characters.

Output

Print a number in the decimal notation without leading zeroes — the result of the permutation.

If it is impossible to rearrange the digits of the number a in the required manner, print 0.

Examples

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
    cnt = [0] * 10
    for i in (1, 6, 8, 9):
        cnt[i] = -1
    for i in a:
        cnt[int(i)] += 1
    
    mod = [1869, 1968, 9816, 6198, 1698, 1986, 1896, 1869]
    modCnt = 0
    
    for i in range(1, 10):
        for j in range(cnt[i]):
            modCnt = (modCnt * 3 + i) % 7
    
    result = ""
    for i in range(1, 10):
        result += str(i) * cnt[i]
    
    modCnt = 10000 * modCnt % 7
    result += str(mod[7 - modCnt]) + '0' * cnt[0]
    
    return result