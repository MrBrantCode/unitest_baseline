"""
QUESTION:
You are given an array $a$ of $n$ positive integers numbered from $1$ to $n$. Let's call an array integral if for any two, not necessarily different, numbers $x$ and $y$ from this array, $x \ge y$, the number $\left \lfloor \frac{x}{y} \right \rfloor$ ($x$ divided by $y$ with rounding down) is also in this array.

You are guaranteed that all numbers in $a$ do not exceed $c$. Your task is to check whether this array is integral.


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Description of the test cases follows.

The first line of each test case contains two integers $n$ and $c$ ($1 \le n \le 10^6$, $1 \le c \le 10^6$) — the size of $a$ and the limit for the numbers in the array.

The second line of each test case contains $n$ integers $a_1$, $a_2$, ..., $a_n$ ($1 \le a_i \le c$) — the array $a$.

Let $N$ be the sum of $n$ over all test cases and $C$ be the sum of $c$ over all test cases. It is guaranteed that $N \le 10^6$ and $C \le 10^6$.


-----Output-----

For each test case print Yes if the array is integral and No otherwise.


-----Examples-----

Input
4
3 5
1 2 5
4 10
1 3 3 7
1 2
2
1 1
1
Output
Yes
No
No
Yes
Input
1
1 1000000
1000000
Output
No


-----Note-----

In the first test case it is easy to see that the array is integral:

$\left \lfloor \frac{1}{1} \right \rfloor = 1$, $a_1 = 1$, this number occurs in the arry

$\left \lfloor \frac{2}{2} \right \rfloor = 1$

$\left \lfloor \frac{5}{5} \right \rfloor = 1$

$\left \lfloor \frac{2}{1} \right \rfloor = 2$, $a_2 = 2$, this number occurs in the array

$\left \lfloor \frac{5}{1} \right \rfloor = 5$, $a_3 = 5$, this number occurs in the array

$\left \lfloor \frac{5}{2} \right \rfloor = 2$, $a_2 = 2$, this number occurs in the array

Thus, the condition is met and the array is integral.

In the second test case it is enough to see that

$\left \lfloor \frac{7}{3} \right \rfloor = \left \lfloor 2\frac{1}{3} \right \rfloor = 2$, this number is not in $a$, that's why it is not integral.

In the third test case $\left \lfloor \frac{2}{2} \right \rfloor = 1$, but there is only $2$ in the array, that's why it is not integral.
"""

def is_integral_array(a, c):
    """
    Check if the given array is integral.

    An array is considered integral if for any two numbers x and y (x >= y) in the array,
    the result of floor(x / y) is also in the array.

    Parameters:
    a (list of int): The array of integers.
    c (int): The limit for the numbers in the array.

    Returns:
    bool: True if the array is integral, False otherwise.
    """
    s = set(a)
    n = len(a)
    
    if 1 not in s:
        return False
    
    k = 0
    for i in range(1, c + 1):
        if i not in s:
            for j in range(n):
                if a[j] > c // i:
                    break
                while k < n and a[k] < i * a[j]:
                    k += 1
                if k < n and a[k] < (i + 1) * a[j]:
                    return False
    return True