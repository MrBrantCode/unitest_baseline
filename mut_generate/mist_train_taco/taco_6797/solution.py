"""
QUESTION:
Gandalf the Grey is in trouble as Saurons eye Rearrived in the middle
    world. Now he has to prepare for the war, But in order to defeat Sauron 
    he has to know the power of saurons eye on the day in which he wants to
    attack.
    
    According to the Elves(Good Friends of Gandalf),Gandalf came to know that
    saurons eye power on current day is equal to 3 time to its power on
    previous day minus the power on a day before previous day.

    Now Gandalf ask Frodo to give him the power of the Saurons Eye on nth day, but poor Frodo is not
    good in mathematics so he ask for help from you.
    Given the nth day you have to give Frodo power of Saurons eye on 
    that day mod 10^9 + 7.
    
Note You can assume the power of sauron eye is 1 on 1st day 
     and 3 on 2nd day.
Input

The first line of the input contains an integer T, the number of test cases. Each of the following T lines contains a single integer N 
denoting the day for which you have to calculate power of Saurons Eye.
Output

For each test case output a single integer in a separate line, the answer for the corresponding test case.

Constraints
1 ≤ T ≤ 10000
1 ≤ N ≤ 10^12SAMPLE INPUT
2
1
3

SAMPLE OUTPUT
1
8

Explanation

First test Case: As indicated in the question power on first day is 1
Second test Case: Answer will be 3*3-1=8.
"""

def calculate_sauron_power(T, N):
    mod = 10**9 + 7
    
    def foo(n):
        while n < 0:
            n += mod
        return n
    
    def matrixMul(a, b):
        x1 = foo((a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod)
        x2 = foo((a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod)
        x3 = foo((a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod)
        x4 = foo((a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod)
        return [[x1, x2], [x3, x4]]
    
    def identity():
        return [[1, 0], [0, 1]]
    
    def matrixExp(m, pow):
        if pow == 0:
            return identity()
        d = matrixExp(m, pow // 2)
        if pow & 1:
            return matrixMul(matrixMul(d, d), m)
        else:
            return matrixMul(d, d)
    
    mm = [[3, -1], [1, 0]]
    results = []
    
    for n in N:
        if n == 1:
            results.append(1)
        elif n == 2:
            results.append(3)
        else:
            n -= 2
            d = matrixExp(mm, n)
            results.append(foo((3 * d[0][0] + d[0][1]) % mod))
    
    return results