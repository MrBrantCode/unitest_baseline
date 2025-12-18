"""
QUESTION:
Samu had come up with new type of numbers, she named them Special Coprime numbers. Special Coprime numbers follow a property  : A number N is said to be Special Coprime if sum of its digits as well as the sum of the squares of its digits are coprime to each other. 

Now she started counting numbers that are Special Coprime. But soon she get bored and decided to write a program that can help do it. Now she want you to help her to find count of such numbers between L and R , where both L and R are included.

Input Format :   First line contain number of test cases T. Each test case contains two space separated integers L and R, denoting the range in which you need to find the count of Special Coprime numbers.

Output Format :   For each test case you need to print the count of such numbers in range [L,R]

Constraints :
1 ≤ T ≤ 10^3
1 ≤ L ≤ R ≤ 10^18

SAMPLE INPUT
1
5 15

SAMPLE OUTPUT
3

Explanation

Between 5 and 15 there are 3 Special Coprime numbers : 10 , 12 , 14
"""

from math import gcd

def count_special_coprime_numbers(test_cases):
    def solveDP(pos, sumD, sumSq, check):
        if pos == -1:
            return 1 if gcd(sumD, sumSq) == 1 else 0

        if not check and dp[pos][sumD][sumSq] != -1:
            return dp[pos][sumD][sumSq]
        
        ans, endDig = 0, 0
        endDig = digits[pos] if check else 9

        for curDig in range(0, endDig + 1):
            ans += solveDP(pos - 1, sumD + curDig, sumSq + curDig * curDig, check and curDig == endDig)

        if not check:
            dp[pos][sumD][sumSq] = ans
        return ans

    def solve(N):
        if N == 0:
            return 0
        length = 0
        while N:
            digits[length] = N % 10
            N //= 10
            length += 1
        return solveDP(length - 1, 0, 0, 1)

    results = []
    dp = [[[-1] * 1500 for i in range(200)] for j in range(20)]
    digits = [0] * 20

    for l, r in test_cases:
        results.append(solve(r) - solve(l - 1))
    
    return results