"""
QUESTION:
Little Elephant from the Zoo of Lviv hates exams. Since Little Elephant lives in Ukraine, he is going to take exams called 'ZNO'. Help him.
There will be n tickets on the table. Each ticket has a number written on it. The i-th ticket can be numbered A_{i} with probability P_{i} percent and with probability 100-P_{i} percent it can be numbered B_{i}. It can not have any other number. A numbering of tickets on the table is correct if and only if all tickets have distinct ticket numbers.

Help Little Elephant find the probability that the numbering will be correct.

------ Input ------ 

The first line of the input contains a single integer T - the number of test cases. T test cases follow. The first line of each test case contains a single integer n - the number of tickets on the table. n lines will follow. Each of these lines contains three integers: P_{i},  A_{i} and B_{i}.

------ Output ------ 

Output T lines, each containing a single real number - answer for the corresponding test case. Rounding errors less than 10^{-6} will be ignored.

------ Constraints ------ 

1 ≤ T ≤ 10

1 ≤ n ≤ 50

1 ≤ A_{i}, B_{i} ≤ 16

0 ≤ P_{i} ≤ 100

----- Sample Input 1 ------ 
2
2
50 1 2
50 2 1
3
100 1 3
47 2 1
74 3 2
----- Sample Output 1 ------ 
0.500000000
0.347800000
"""

def calculate_correct_numbering_probability(test_cases):
    MAX_N = 16

    def test(x, bit):
        return x >> bit & 1

    results = []

    for test_case in test_cases:
        n = len(test_case)
        if n > MAX_N:
            results.append(0.0)
            continue

        dp = {0: 1.0}

        for (pr, a, b) in test_case:
            pr_a = 0.01 * pr
            pr_b = 1 - pr_a
            a -= 1
            b -= 1
            next_dp = {}
            for (mask, prob) in dp.items():
                if not test(mask, a):
                    next_mask = mask | 1 << a
                    next_dp[next_mask] = next_dp.get(next_mask, 0) + prob * pr_a
                if not test(mask, b):
                    next_mask = mask | 1 << b
                    next_dp[next_mask] = next_dp.get(next_mask, 0) + prob * pr_b
            dp = next_dp

        results.append(sum(dp.values()))

    return results