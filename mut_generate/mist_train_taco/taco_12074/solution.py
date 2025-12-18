"""
QUESTION:
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.


Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.


Note:


       K will be an integer in the range [0, 10^9].
"""

def count_factorials_with_trailing_zeroes(K: int) -> int:
    def count_trailing_zeroes(n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

    low, high = 0, 5 * (K + 1)
    while low <= high:
        mid = (low + high) // 2
        if count_trailing_zeroes(mid) < K:
            low = mid + 1
        else:
            high = mid - 1
    
    if count_trailing_zeroes(low) == K:
        return 5
    else:
        return 0