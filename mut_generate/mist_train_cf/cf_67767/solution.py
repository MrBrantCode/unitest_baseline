"""
QUESTION:
Function `guess_number` with parameters `n` and `pick` and `t`. Given API `guess(num)` that provides hints about the number to be guessed, which lies `t` percent of the time. The task is to return the number that was chosen, under the restrictions that `1 <= n <= 2^31 - 1`, `1 <= pick <= n`, and `0 <= t <= 100`.
"""

def guess_number(n: int, pick: int, t: int) -> int:
    def guess(num: int) -> int:
        if num == pick:
            return 0
        elif num < pick:
            return 1
        else:
            return -1

    def helper(l, r):
        if l > r:
            return l
        mid = (l + r) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif (res == 1 and t > 50) or (res == -1 and t < 50):
            return helper(mid + 1, r)
        else:
            return helper(l, mid - 1)

    return helper(1, n)