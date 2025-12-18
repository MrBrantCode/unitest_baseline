"""
QUESTION:
Given a number num. You are tasked with finding the smallest number S, such that num is a factor of S! (S factorial).
 
Example 1:
Input: num = 6
Output: 3
Explanation: 3! = 6 and 6 is
divisible by 6.
Example 2:
Input: num = 800
Output: 10
Exaplantion: 10! = 3628800 and 3628800 
is divisible by 800.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function findFact() which takes num as input parameter and returns smallest number whose factorial is divisible by num.
 
Expected Space Complexity: O(sqrt(num))
Expected Space Compplexity: O(sqrt(num))
 
Constraints:
1 <= num <= 10^{12}
"""

from collections import defaultdict
import math

def find_smallest_factorial_divisor(num: int) -> int:
    def ok(mi, k, v):
        ans = 0
        while mi > 0:
            ans += mi // k
            mi //= k
            if ans >= v:
                return True
        return ans >= v

    def search(k, v):
        lo, hi = 1, 1000001
        ans = 0
        while lo <= hi:
            mi = (lo + hi) // 2
            if ok(mi, k, v):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans

    if num == 1:
        return 1
    
    d = defaultdict(int)
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            d[i] += 1
            num //= i
    if num != 1:
        d[num] = 1
    
    ans = 0
    for k, v in d.items():
        if v == 1:
            ans = max(ans, k)
        else:
            ans = max(ans, search(k, v))
    
    return ans