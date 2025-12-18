"""
QUESTION:
Suppose you have two polynomials <image> and <image>. Then polynomial <image> can be uniquely represented in the following way:

<image>

This can be done using [long division](https://en.wikipedia.org/wiki/Polynomial_long_division). Here, <image> denotes the degree of polynomial P(x). <image> is called the remainder of division of polynomial <image> by polynomial <image>, it is also denoted as <image>. 

Since there is a way to divide polynomials with remainder, we can define Euclid's algorithm of finding the greatest common divisor of two polynomials. The algorithm takes two polynomials <image>. If the polynomial <image> is zero, the result is <image>, otherwise the result is the value the algorithm returns for pair <image>. On each step the degree of the second argument decreases, so the algorithm works in finite number of steps. But how large that number could be? You are to answer this question. 

You are given an integer n. You have to build two polynomials with degrees not greater than n, such that their coefficients are integers not exceeding 1 by their absolute value, the leading coefficients (ones with the greatest power of x) are equal to one, and the described Euclid's algorithm performs exactly n steps finding their greatest common divisor. Moreover, the degree of the first polynomial should be greater than the degree of the second. By a step of the algorithm we mean the transition from pair <image> to pair <image>. 

Input

You are given a single integer n (1 ≤ n ≤ 150) — the number of steps of the algorithm you need to reach.

Output

Print two polynomials in the following format.

In the first line print a single integer m (0 ≤ m ≤ n) — the degree of the polynomial. 

In the second line print m + 1 integers between  - 1 and 1 — the coefficients of the polynomial, from constant to leading. 

The degree of the first polynomial should be greater than the degree of the second polynomial, the leading coefficients should be equal to 1. Euclid's algorithm should perform exactly n steps when called using these polynomials.

If there is no answer for the given n, print -1.

If there are multiple answer, print any of them.

Examples

Input

1


Output

1
0 1
0
1


Input

2


Output

2
-1 0 1
1
0 1

Note

In the second example you can print polynomials x2 - 1 and x. The sequence of transitions is

(x2 - 1, x) → (x, - 1) → ( - 1, 0).

There are two steps in it.
"""

def generate_polynomials_for_gcd_steps(n):
    if n < 1:
        return None
    
    class polynomial:
        def __init__(self, data):
            self.data = data

        def __lshift__(self, x):
            return polynomial([0] * x + self.data)

        def __len__(self):
            return len(self.data)

        def __sub__(self, other):
            newData = [y - x for (y, x) in zip(self.data, other.data + [0] * 1000)]
            while len(newData) > 0 and newData[-1] == 0:
                del newData[-1]
            return polynomial(newData)

        def __add__(self, other):
            newData = [(y + x) % 2 for (y, x) in zip(self.data + [0] * 1000, other.data + [0] * 1000)]
            while len(newData) > 0 and newData[-1] == 0:
                del newData[-1]
            return polynomial(newData)

        def __mul__(self, amt):
            return polynomial([x * amt for x in self.data])

        def __getitem__(self, idx):
            return self.data[idx]

        def __mod__(self, other):
            tmp = self
            times = 0
            while len(tmp) >= len(other):
                times += 1
                if times > 1000:
                    print(*tmp.data)
                    print(*other.data)
                    exit(0)
                tmp = tmp - (other << len(tmp) - len(other)) * (tmp[-1] // other[-1])
            return tmp

    def gcdSteps(p1, p2, steps=0):
        if len(p1) == 0 or len(p2) == 0:
            return steps
        else:
            return gcdSteps(p2, p1 % p2, steps + 1)

    (a, b) = (polynomial([0, 1]), polynomial([1]))
    for i in range(n - 1):
        if gcdSteps(a, b) != i + 1:
            return None
        (a, b) = (b + (a << 1), a)

    return a.data, b.data