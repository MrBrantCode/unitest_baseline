"""
QUESTION:
Petya loves lucky numbers. Everybody knows that positive integers are lucky if their decimal representation doesn't contain digits other than 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Lucky number is super lucky if it's decimal representation contains equal amount of digits 4 and 7. For example, numbers 47, 7744, 474477 are super lucky and 4, 744, 467 are not.

One day Petya came across a positive integer n. Help him to find the least super lucky number which is not less than n.

Input

The only line contains a positive integer n (1 ≤ n ≤ 109). This number doesn't have leading zeroes.

Output

Output the least super lucky number that is more than or equal to n.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specificator.

Examples

Input

4500


Output

4747


Input

47


Output

47
"""

def find_least_super_lucky_number(n):
    gh = set()

    def rep(num, four, seven):
        if num > 10000000000:
            return
        if four == seven:
            gh.add(num)
        rep(num * 10 + 4, four + 1, seven)
        rep(num * 10 + 7, four, seven + 1)

    rep(0, 0, 0)
    gh = sorted(gh)

    def bin_s(a):
        lo = 0
        hi = len(gh)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if gh[mid] >= a:
                ans = gh[mid]
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    return bin_s(n)