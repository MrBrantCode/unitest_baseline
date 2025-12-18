"""
QUESTION:
A professor invented Cookie Breeding Machine for his students who like cookies very much.

When one cookie with the taste of x is put into the machine and a non-negative integer y less than or equal to 127 is input on the machine, it consumes the cookie and generates two cookies with the taste of y and (x XOR y).

Here, XOR represents Bitwise Exclusive OR.

At first, there is only one cookie and the taste of it is D .

Find the maximum value of the sum of the taste of the exactly N cookies generated after the following operation is conducted N-1 times.

1. Put one of the cookies into the machine.
2. Input a non-negative integer less than or equal to 127 on the machine.

Constraints

* 1 \leq T \leq 1000
* 1 \leq N_t \leq 1000 (1 \leq t \leq T)
* 1 \leq D_t \leq 127 (1 \leq t \leq T)

Input

The input is given from Standard Input in the following format:


T
N_1 D_1
:
N_T D_T


The input consists of multiple test cases. An Integer T that represents the number of test cases is given on line 1.
Each test case is given on the next T lines.
In the t-th test case ( 1 \leq t \leq T ), N_t that represents the number of cookies generated through the operations and D_t that represents the taste of the initial cookie are given separated by space.


Output

For each test case, print the maximum value of the sum of the taste of the N cookies generated through the operations on one line.

Example

Input

3
3 1
4 108
1 10


Output

255
400
10
"""

def calculate_max_cookie_taste(T, test_cases):
    results = []
    for i in range(T):
        N, D = test_cases[i]
        if N & 1 == 0:
            D ^= 127
        results.append(D + (N - 1) * 127)
    return results