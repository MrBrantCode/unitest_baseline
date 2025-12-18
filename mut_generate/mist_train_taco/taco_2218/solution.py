"""
QUESTION:
Integer factorisation is hard. The RSA Factoring Challenge offered $100 000 for factoring RSA-1024, a 1024-bit long product of two prime numbers. To this date, nobody was able to claim the prize. We want you to factorise a 1024-bit number.

Since your programming language of choice might not offer facilities for handling large integers, we will provide you with a very simple calculator. 

To use this calculator, you can print queries on the standard output and retrieve the results from the standard input. The operations are as follows: 

  * + x y where x and y are integers between 0 and n-1. Returns (x+y) mod n. 
  * - x y where x and y are integers between 0 and n-1. Returns (x-y) mod n. 
  * * x y where x and y are integers between 0 and n-1. Returns (x ⋅ y) mod n. 
  * / x y where x and y are integers between 0 and n-1 and y is coprime with n. Returns (x ⋅ y^{-1}) mod n where y^{-1} is multiplicative inverse of y modulo n. If y is not coprime with n, then -1 is returned instead. 
  * sqrt x where x is integer between 0 and n-1 coprime with n. Returns y such that y^2 mod n = x. If there are multiple such integers, only one of them is returned. If there are none, -1 is returned instead. 
  * ^ x y where x and y are integers between 0 and n-1. Returns {x^y mod n}. 



Find the factorisation of n that is a product of between 2 and 10 distinct prime numbers, all of form 4x + 3 for some integer x.

Because of technical issues, we restrict number of requests to 100.

Input

The only line contains a single integer n (21 ≤ n ≤ 2^{1024}). It is guaranteed that n is a product of between 2 and 10 distinct prime numbers, all of form 4x + 3 for some integer x.

Output

You can print as many queries as you wish, adhering to the time limit (see the Interaction section for more details). 

When you think you know the answer, output a single line of form ! k p_1 p_2 ... p_k, where k is the number of prime factors of n, and p_i are the distinct prime factors. You may print the factors in any order.

Hacks input

For hacks, use the following format:. 

The first should contain k (2 ≤ k ≤ 10) — the number of prime factors of n. 

The second should contain k space separated integers p_1, p_2, ..., p_k (21 ≤ n ≤ 2^{1024}) — the prime factors of n. All prime factors have to be of form 4x + 3 for some integer x. They all have to be distinct. 

Interaction

After printing a query do not forget to output end of line and flush the output. Otherwise you will get Idleness limit exceeded. To do this, use:

  * fflush(stdout) or cout.flush() in C++;
  * System.out.flush() in Java;
  * flush(output) in Pascal;
  * stdout.flush() in Python;
  * see documentation for other languages.



The number of queries is not limited. However, your program must (as always) fit in the time limit. The run time of the interactor is also counted towards the time limit. The maximum runtime of each query is given below.

  * + x y — up to 1 ms. 
  * - x y — up to 1 ms. 
  * * x y — up to 1 ms. 
  * / x y — up to 350 ms. 
  * sqrt x — up to 80 ms. 
  * ^ x y — up to 350 ms. 



Note that the sample input contains extra empty lines so that it easier to read. The real input will not contain any empty lines and you do not need to output extra empty lines.

Example

Input

21

7

17

15

17

11

-1

15



Output

+ 12 16

- 6 10

* 8 15

/ 5 4

sqrt 16

sqrt 5

^ 6 12

! 2 3 7

Note

We start by reading the first line containing the integer n = 21. Then, we ask for: 

  1. (12 + 16) mod 21 = 28 mod 21 = 7. 
  2. (6 - 10) mod 21 = -4 mod 21 = 17. 
  3. (8 ⋅ 15) mod 21 = 120 mod 21 = 15. 
  4. (5 ⋅ 4^{-1}) mod 21 = (5 ⋅ 16) mod 21 = 80 mod 21 = 17. 
  5. Square root of 16. The answer is 11, as (11 ⋅ 11) mod 21 = 121 mod 21 = 16. Note that the answer may as well be 10. 
  6. Square root of 5. There is no x such that x^2 mod 21 = 5, so the output is -1. 
  7. (6^{12}) mod 21 = 2176782336 mod 21 = 15. 



We conclude that our calculator is working, stop fooling around and realise that 21 = 3 ⋅ 7.
"""

import random

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def isPrime(n):
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert 2 ** s * d == n - 1

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True
    for i in range(20):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True

def factorize_rsa_number(n, calculator):
    divs = [n]
    while not all([isPrime(x) for x in divs]):
        x = random.randint(1, n - 1)
        result = calculator('sqrt', x * x % n)
        x += result
        tmp = []
        for it in divs:
            g = gcd(x, it)
            if g != 1:
                tmp.append(g)
            if it // g != 1:
                tmp.append(it // g)
        divs = tmp
    divs = list(set(divs) - {1})
    return divs