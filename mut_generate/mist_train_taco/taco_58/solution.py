"""
QUESTION:
Snuke found a random number generator. It generates an integer between 0 and 2^N-1 (inclusive). An integer sequence A_0, A_1, \cdots, A_{2^N-1} represents the probability that each of these integers is generated. The integer i (0 \leq i \leq 2^N-1) is generated with probability A_i / S, where S = \sum_{i=0}^{2^N-1} A_i. The process of generating an integer is done independently each time the generator is executed.

Snuke has an integer X, which is now 0. He can perform the following operation any number of times:

* Generate an integer v with the generator and replace X with X \oplus v, where \oplus denotes the bitwise XOR.



For each integer i (0 \leq i \leq 2^N-1), find the expected number of operations until X becomes i, and print it modulo 998244353. More formally, represent the expected number of operations as an irreducible fraction P/Q. Then, there exists a unique integer R such that R \times Q \equiv P \mod 998244353,\ 0 \leq R < 998244353, so print this R.

We can prove that, for every i, the expected number of operations until X becomes i is a finite rational number, and its integer representation modulo 998244353 can be defined.

Constraints

* 1 \leq N \leq 18
* 1 \leq A_i \leq 1000
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_0 A_1 \cdots A_{2^N-1}


Output

Print 2^N lines. The (i+1)-th line (0 \leq i \leq 2^N-1) should contain the expected number of operations until X becomes i, modulo 998244353.

Examples

Input

2
1 1 1 1


Output

0
4
4
4


Input

2
1 2 1 2


Output

0
499122180
4
499122180


Input

4
337 780 799 10 796 875 331 223 941 67 148 483 390 565 116 355


Output

0
468683018
635850749
96019779
657074071
24757563
745107950
665159588
551278361
143136064
557841197
185790407
988018173
247117461
129098626
789682908
"""

MOD = 998244353

def calculate_expected_operations(N, A):
    NN = 1 << N
    
    def fwht(a):
        i = 1
        while i < NN:
            j = 0
            while j < NN:
                for k in range(i):
                    (x, y) = (a[j + k], a[i + j + k])
                    (a[j + k], a[i + j + k]) = ((x + y) % MOD, (x - y) % MOD)
                j += i << 1
            i <<= 1
    
    def inv(x):
        return pow(x, MOD - 2, MOD)
    
    s = inv(sum(A) % MOD)
    for i in range(NN):
        A[i] = A[i] * s % MOD
    A[0] = (A[0] - 1) % MOD
    fwht(A)
    
    B = [-1] * NN
    B[0] = (NN - 1) % MOD
    fwht(B)
    
    C = [inv(A[i]) * B[i] % MOD for i in range(NN)]
    fwht(C)
    
    for i in range(NN):
        C[i] = C[i] * inv(NN) % MOD
    
    result = [(C[i] - C[0]) % MOD for i in range(NN)]
    return result