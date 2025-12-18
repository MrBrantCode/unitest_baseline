"""
QUESTION:
Eugene must do his homework, but he is struggling. 

He has three integer numbers: A, N, M. He writes number A on the board N times in a row. Let's call the resulting big number X.
Help Eugene find X modulo M. 

Input Format

First line contains T, the number of testcases. 

Each testcase contains three numbers: A, N, M separated by a single space.   

Constraints

$1\leq T\leq200$  
${0}\leq A\leq10^3$  
$0<N<10^{12}$    
$1<M<10^9$    

Output Format

Print the required answer for each testcase in a new line.

Sample Input
2  
12 2 17  
523 3 11  

Sample Output
5
6

Explanation

First testcase:

A = 12

N = 2

X = 1212

1212 modulo 17 = 5

Second testcase:

A = 523

N = 3

X = 523523523

523523523 modulo 11 = 6
"""

def calculate_modulo(A, N, M):
    def S(A, l, N, M):
        if N == 0:
            return A % M
        if N % 2 == 0:
            return (S(A, l, N - 1, M) * l + S(A, l, 0, M)) % M
        z = S(A, l, N // 2, M)
        return z * (pow(l, N // 2 + 1, M) + 1) % M

    def S1(A, N, M):
        return S(A, 10 ** len(str(A)), N - 1, M)

    return S1(A, N, M)