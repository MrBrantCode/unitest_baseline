"""
QUESTION:
Pseudo-code to find the nth fibonacci number :

int fibo(int n)
{
   if (n == 0)
{
   write(0)
   return 0
}
if (n == 1)
{
   write(1)
   return 1
}
return fibo(n - 1) + fibo(n - 2)
}
If we call fibo(3),  the following happens:

fibo(3) calls fibo(2) and fibo(1) ---->the first call.

fibo(2) calls fibo(1) ---->the second call and fibo(0).

The second call of fibo(1) writes 1 and returns 1.

fibo(0) writes 0 and returns 0.

fibo(2) gets the results of fibo(1) and fibo(0) and returns 1.

The first call of fibo(1) writes 1 and returns 1.

fibo(3) gets the results of fibo(2) and fibo(1) and returns 2.

All in all, 1 will be written twice and 0 will be written once. Now find how many times 0 and 1 will be written for a given integer N.

INPUT

The first line contains an integer T, denoting the number of test cases. The next T lines contain an integer N.

OUTPUT

For each test case, print the output in one line which consists of 2 space separated integers. The first integer denotes the number of times 0 gets printed , while the  second integer denotes the number of times 1 gets printed.

CONSTRAINTS

1 ≤ T ≤ 50

0 ≤ N ≤ 40

SAMPLE INPUT
2
1
2

SAMPLE OUTPUT
0 1
1 1
"""

def count_fibonacci_prints(T, N_list):
    # Precompute the counts of 0s and 1s for Fibonacci numbers up to 40
    L = [[1, 0], [0, 1]]
    for y in range(2, 41):
        Z = L[y-1][0] + L[y-2][0]
        V = L[y-1][1] + L[y-2][1]
        L.append([Z, V])
    
    # Initialize the result list
    result = []
    
    # Process each test case
    for N in N_list:
        result.append((L[N][0], L[N][1]))
    
    return result