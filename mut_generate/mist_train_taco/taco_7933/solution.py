"""
QUESTION:
You are given a sequence of n integers a_1, a_2, ..., a_{n}. 

Determine a real number x such that the weakness of the sequence a_1 - x, a_2 - x, ..., a_{n} - x is as small as possible.

The weakness of a sequence is defined as the maximum value of the poorness over all segments (contiguous subsequences) of a sequence.

The poorness of a segment is defined as the absolute value of sum of the elements of segment.


-----Input-----

The first line contains one integer n (1 ≤ n ≤ 200 000), the length of a sequence.

The second line contains n integers a_1, a_2, ..., a_{n} (|a_{i}| ≤ 10 000).


-----Output-----

Output a real number denoting the minimum possible weakness of a_1 - x, a_2 - x, ..., a_{n} - x. Your answer will be considered correct if its relative or absolute error doesn't exceed 10^{ - 6}.


-----Examples-----
Input
3
1 2 3

Output
1.000000000000000

Input
4
1 2 3 4

Output
2.000000000000000

Input
10
1 10 2 9 3 8 4 7 5 6

Output
4.500000000000000



-----Note-----

For the first case, the optimal value of x is 2 so the sequence becomes  - 1, 0, 1 and the max poorness occurs at the segment "-1" or segment "1". The poorness value (answer) equals to 1 in this case. 

For the second sample the optimal value of x is 2.5 so the sequence becomes  - 1.5,  - 0.5, 0.5, 1.5 and the max poorness occurs on segment "-1.5 -0.5" or "0.5 1.5". The poorness value (answer) equals to 2 in this case.
"""

def minimize_weakness(nums):
    def max_sum(nums, shift):
        res = 0
        res_m = 0
        cur_sum = 0
        cur_m_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i] + shift
            cur_m_sum += nums[i] + shift
            res = max(res, cur_sum)
            cur_sum = max(0, cur_sum)
            res_m = min(res_m, cur_m_sum)
            cur_m_sum = min(0, cur_m_sum)
        return (res, -res_m)

    def weaks(nums, shift):
        return max_sum(nums, shift)

    l = -10000
    r = 10000
    ans = max(weaks(nums, 0))
    w1 = 1
    w2 = -1
    PREC = 10 ** (-6)
    while abs(w1 - w2) >= PREC and abs(w1 - w2) > PREC * max(w1, w2):
        m = (r + l) / 2
        (w1, w2) = weaks(nums, m)
        if w1 > w2:
            r = m
        else:
            l = m
    return (w1 + w2) / 2