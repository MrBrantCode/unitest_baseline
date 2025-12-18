"""
QUESTION:
Help Shashank in calculating the value of $\mbox{S}$, which is given as follows. Since the value of $\mbox{S}$ can be very large, he only wants the last 2 digits of $\mbox{S}$.

$S=1^N+2^N+3^N+\cdots+K^N$

Input Format 

The first line contains an integer $\mathbf{T}$ i.e. number of the test cases. 

The next $\mathbf{T}$ lines will each contain a pair of integers, i.e. $\mbox{K}$ and $N$.  

Output Format 

Print the last two digits of $\mbox{S}$ for each test case in separate lines.  

Constraints 

$1\leq T\leq10^4$ 

$2\leq K\leq10^{16}$ 

$2\leq N\leq10^{16}$  

Sample Input#00  

3
2 2
2 3
3 3

Sample Output#00  

05
09
36

Sample Input#01  

3
5 2
3 4
3 3

Sample Output#01  

55
98
36

Explanation

For the first test case, $1^2+2^2+3^2+4^2+5^2=55$
"""

def calculate_last_two_digits(T, test_cases):
    results = []
    for k, n in test_cases:
        k += 1
        full = sum((pow(i, n, 100) for i in range(100))) % 100
        tail = sum((pow(i, n, 100) for i in range(k % 100))) % 100
        ans = (full * (k // 100) + tail) % 100
        results.append('{:02d}'.format(ans))
    return results