"""
QUESTION:
Aklank is fond of numbers which are divisible by either P1 or P2. He termed those numbers as Bakku numbers. Recently his best friend gave him a range of numbers. Now he is wondering what is the probability of finding Bakku numbers from that range of numbers.

Input
First line of input contains two integers P1 and P2 (2 ≤ P1 ≤ 10000, 2 ≤ P2 ≤ 10000) — both P1 and P2 are prime numbers.

Second line of the input contains an integer T  (1 ≤ T ≤ 100000) — the number of test cases.

Each of the next T lines contains two integers - L and R (1 ≤ L ≤ R ≤ 100,00,00,000) - the starting number and ending number of each range from where he will search for Bakku numbers (inclusive).

Output
Print T lines for each test case.

In each line print answer with up to 6 digits after decimal point.

SAMPLE INPUT
3 5
2
1 10
20 34

SAMPLE OUTPUT
0.500000
0.466667

Explanation

First Case : Numbers divisible by 3 or 5 are 3, 5, 6, 9, 10

Second Case : Numbers divisible by 3 or 5 are 20, 21, 24, 25, 27, 30, 33
"""

def calculate_bakku_probability(p1, p2, test_cases):
    results = []
    for (l, r) in test_cases:
        t1 = r // p1 - l // p1
        if l % p1 == 0:
            t1 += 1
        
        t2 = r // p2 - l // p2
        if l % p2 == 0:
            t2 += 1
        
        com = p1 * p2
        t3 = r // com - l // com
        if l % com == 0:
            t3 += 1
        
        x = t1 + t2 - t3
        val = x / float(r - l + 1)
        results.append('{:.6f}'.format(val))
    
    return results