"""
QUESTION:
You are given an integer N. Among the integers between 1 and N (inclusive), how many Shichi-Go-San numbers (literally "Seven-Five-Three numbers") are there?
Here, a Shichi-Go-San number is a positive integer that satisfies the following condition:
 - When the number is written in base ten, each of the digits 7, 5 and 3 appears at least once, and the other digits never appear.

-----Constraints-----
 - 1 \leq N < 10^9
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the number of the Shichi-Go-San numbers between 1 and N (inclusive).

-----Sample Input-----
575

-----Sample Output-----
4

There are four Shichi-Go-San numbers not greater than 575: 357, 375, 537 and 573.
"""

def count_shichi_go_san_numbers(N: int) -> int:
    def dfs(s: str) -> int:
        if int(s) > N:
            return 0
        ret = 1 if all(s.count(c) > 0 for c in '357') else 0
        for c in '357':
            ret += dfs(s + c)
        return ret
    
    return dfs('0')