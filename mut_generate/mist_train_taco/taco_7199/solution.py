"""
QUESTION:
Stepan has n pens. Every day he uses them, and on the i-th day he uses the pen number i. On the (n + 1)-th day again he uses the pen number 1, on the (n + 2)-th — he uses the pen number 2 and so on.

On every working day (from Monday to Saturday, inclusive) Stepan spends exactly 1 milliliter of ink of the pen he uses that day. On Sunday Stepan has a day of rest, he does not stend the ink of the pen he uses that day. 

Stepan knows the current volume of ink in each of his pens. Now it's the Monday morning and Stepan is going to use the pen number 1 today. Your task is to determine which pen will run out of ink before all the rest (that is, there will be no ink left in it), if Stepan will use the pens according to the conditions described above.


-----Input-----

The first line contains the integer n (1 ≤ n ≤ 50 000) — the number of pens Stepan has.

The second line contains the sequence of integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9), where a_{i} is equal to the number of milliliters of ink which the pen number i currently has.


-----Output-----

Print the index of the pen which will run out of ink before all (it means that there will be no ink left in it), if Stepan will use pens according to the conditions described above. 

Pens are numbered in the order they are given in input data. The numeration begins from one. 

Note that the answer is always unambiguous, since several pens can not end at the same time.


-----Examples-----
Input
3
3 3 3

Output
2

Input
5
5 4 5 4 4

Output
5



-----Note-----

In the first test Stepan uses ink of pens as follows:   on the day number 1 (Monday) Stepan will use the pen number 1, after that there will be 2 milliliters of ink in it;  on the day number 2 (Tuesday) Stepan will use the pen number 2, after that there will be 2 milliliters of ink in it;  on the day number 3 (Wednesday) Stepan will use the pen number 3, after that there will be 2 milliliters of ink in it;  on the day number 4 (Thursday) Stepan will use the pen number 1, after that there will be 1 milliliters of ink in it;  on the day number 5 (Friday) Stepan will use the pen number 2, after that there will be 1 milliliters of ink in it;  on the day number 6 (Saturday) Stepan will use the pen number 3, after that there will be 1 milliliters of ink in it;  on the day number 7 (Sunday) Stepan will use the pen number 1, but it is a day of rest so he will not waste ink of this pen in it;  on the day number 8 (Monday) Stepan will use the pen number 2, after that this pen will run out of ink. 

So, the first pen which will not have ink is the pen number 2.
"""

def find_first_empty_pen(n, ink_volumes):
    def Min(x, y):
        return y if x > y else x

    def Gcd(x, y):
        return Gcd(y % x, x) if x != 0 else y

    def Lcm(x, y):
        return x * y // Gcd(x, y)

    d = [0] * n
    ok = 0
    cur = 0
    length = Lcm(7, n)

    for i in range(7 * n):
        if ink_volumes[i % n] == 0:
            return i % n + 1
        if cur != 6:
            ink_volumes[i % n] -= 1
            d[i % n] += 1
        cur = (cur + 1) % 7

    if ok == 0:
        k = 10 ** 20
        for i in range(n):
            ink_volumes[i] += d[i]
            if d[i] == 0:
                continue
            if ink_volumes[i] % d[i] > 0:
                k = Min(k, ink_volumes[i] // d[i])
            else:
                k = Min(k, ink_volumes[i] // d[i] - 1)

        if k == 10 ** 20:
            k = 0

        for i in range(n):
            ink_volumes[i] -= k * d[i]

        iter = 0
        cur = 0
        while True:
            if ink_volumes[iter] == 0:
                return iter % n + 1
            else:
                if cur != 6:
                    ink_volumes[iter] -= 1
                cur = (cur + 1) % 7
                iter = (iter + 1) % n