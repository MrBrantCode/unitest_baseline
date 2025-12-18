"""
QUESTION:
Little Dipu is a small kid and like all the other kids, he likes to play, but he plays with numbers (He is extraordinary you know). Now-a-days Dipu has some extra interest in odd numbers. So, he says that a number N is interesting if it has odd number of divisors. Now Dipu turns to you and asks you to tell him how many interesting numbers are there between two given numbers, L and R (both inclusive).
 Input 
First line of input contains the number of test cases T. Each of the next T lines contains two space separated integers L and R.

 Output 
For each test case, output an integer, denoting the count of interesting numbers between L and R (both inclusive).

 Constraints 
1 ≤ T ≤ 100000

1 ≤ L ≤ R ≤ 10^18

SAMPLE INPUT
2
1 3
6 10

SAMPLE OUTPUT
1
1

Explanation

In 1st test case, 1 has 1 divisor, 2 has 2 divisors and 3 also has 2 divisors. So only 1 has odd number of divisors. Hence count of interesting numbers is 1.

In 2nd test case, 9 is the only number to have odd number of divisors. So answer is again 1.
"""

def count_interesting_numbers(T, test_cases):
    results = []
    for l, r in test_cases:
        sl, sr = int(l**0.5), int(r**0.5)
        if sl**2 > l:
            sl = sl - 1
        if sr**2 > r:
            sr = sr - 1
        count = sr - sl + (sl**2 == l)
        results.append(count)
    return results