"""
QUESTION:
Naruto is a fan of numbers, he likes to play with them. This time he decided to multiply numbers and produce output. After every k elements he decides to find x^m, where x is the multiplication till k elements and m is a random number that naruto takes. Help naruto find the output. 

As answer could be large, help him, calculate value modulo w.

Input
T=number of test case
N=number of elements he will enter
K=every kth element
M=Random number
W=Modulo 
A[i]=n elements to be entered.  

Output
Output answer of each test case in one line.  

Constraint:
0<t<100
0<a[i]<10000000
1<n<101
k<100000
m<100000 
w<100000    

SAMPLE INPUT
2
5 2 2 5
1 2 3 4 5
5 2 2 5
1 2 3 4 6

SAMPLE OUTPUT
0
4

Explanation

In first case n=5,k=2,m=2,w=5;
Step 1
1
Step 2: 12=2
since k=2 therefore 2^m=2^2=4;
Step 3: 43=12
Step 4: 124=48
since k=2,therefore 48^m=48^2
step 5: 23045=11520
step 6: 11520%5=0

2nd Test case
Step 1
1
Step 2: 12=2
since k=2 therefore 2^m=2^2=4;
Step 3: 43=12
Step 4: 124=48
since k=2,therefore 48^m=48^2
step 5: 23046=13824
step 6: 13824%5=4
"""

def power1(x, n, MOD):
    if n == 0:
        return 1
    ret = 1
    while n:
        if n & 1:
            ret *= x
            ret %= MOD
        x *= x
        x %= MOD
        n >>= 1
    return ret

def calculate_naruto_output(T, test_cases):
    results = []
    for case in test_cases:
        N, K, M, W, A = case
        prod = 1
        for x in range(N):
            prod = prod * A[x] % W
            if (x + 1) % K == 0:
                prod = power1(prod, M, W)
                prod %= W
            if prod == 0:
                break
        results.append(prod % W)
    return results