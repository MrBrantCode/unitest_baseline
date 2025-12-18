"""
QUESTION:
Given two strings `low` and `high` representing two integers where `low <= high`, write a function `strobogrammaticInRange` to return the number of strobogrammatic numbers in the range `[low, high]`. A strobogrammatic number is a number that looks the same when rotated 180 degrees and must also be a palindrome.

The input strings `low` and `high` have the following constraints: 
`1 <= low.length, high.length <= 15`, 
`low` and `high` consist of only digits, 
`low <= high`, 
`low` and `high` do not contain any leading zeros except for zero itself.
"""

def strobogrammaticInRange(low: str, high: str) -> int:
    count = 0
    lookUp = { 
        '0': '0', 
        '1': '1', 
        '6': '9', 
        '8': '8', 
        '9': '6' 
    }

    pairs = [
        ['0', '0'],
        ['1', '1'],
        ['6', '9'],
        ['8', '8'],
        ['9', '6']
    ]

    def dfs(n, result):
        nonlocal count
        if len(result) > n:
            return 

        if len(result) >= 1 and len(result) <= n and (n != 1 and result[0] != '0') :
            num = int(result)
            if int(low) <= num <= int(high):
                count += 1

        for pair in pairs:
            dfs(n, pair[0] + result + pair[1])

    n1 = len(low)
    n2 = len(high)

    for n in range(n1, n2+1):
        dfs(n, '')

    return count