"""
QUESTION:
A car number in Berland consists of exactly n digits. A number is called beautiful if it has at least k equal digits. Vasya wants to change the digits in his car's number so that the number became beautiful. To replace one of n digits Vasya has to pay the sum of money, equal to the absolute difference between the old digit and the new one.

Help Vasya: find the minimum sum of money he should pay to make the number of his car beautiful. You should also find the resulting beautiful number. If there are several such numbers, then print the lexicographically minimum one.

Input

The first line contains two space-separated integers n and k (2 ≤ n ≤ 104, 2 ≤ k ≤ n) which represent how many digits the number has and how many equal digits a beautiful number should have. The second line consists of n digits. It describes the old number of Vasya's car. It is guaranteed that the number contains no spaces and only contains digits.

Output

On the first line print the minimum sum of money Vasya needs to change the number. On the second line print the car's new number. If there are several solutions, print the lexicographically minimum one.

Examples

Input

6 5
898196


Output

4
888188


Input

3 2
533


Output

0
533


Input

10 6
0001112223


Output

3
0000002223

Note

In the first sample replacing the second digit with an "8" costs |9 - 8| = 1. Replacing the fifth digit with an "8" costs the same. Replacing the sixth digit costs |6 - 8| = 2. As a result, Vasya will pay 1 + 1 + 2 = 4 for a beautiful number "888188".

The lexicographical comparison of strings is performed by the < operator in modern programming languages. The string x is lexicographically smaller than the string y, if there exists such i (1 ≤ i ≤ n), that xi < yi, and for any j (1 ≤ j < i) xj = yj. The strings compared in this problem will always have the length n.
"""

def make_beautiful_car_number(n, k, car_number):
    from math import inf

    def fun(a):
        if a[1] == 0:
            return a
        else:
            return (a[0], a[1], -a[2])
        return a

    def operate(x):
        ans = list(car_number)
        c = []
        for i in range(n):
            c.append((abs(x - int(car_number[i])), int(x > int(car_number[i])), i))
        c.sort(key=fun)
        cost = 0
        for i in range(k):
            cost += c[i][0]
            ans[c[i][-1]] = str(x)
        return (cost, ''.join(ans))

    min_cost = inf
    beautiful_number = car_number
    for i in range(10):
        (cost, t) = operate(i)
        if cost < min_cost:
            min_cost = cost
            beautiful_number = t
        elif cost == min_cost:
            beautiful_number = min(beautiful_number, t)

    return min_cost, beautiful_number