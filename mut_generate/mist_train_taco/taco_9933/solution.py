"""
QUESTION:
A recent lab accident resulted in the creation of an extremely dangerous virus that replicates so rapidly it's hard to predict exactly how many cells it will contain after a given period of time. However, a lab technician made the following observations about its growth per millisecond:

The probability of the number of virus cells growing by a factor of ${a}$ is $0.5$.
The probability of the number of virus cells growing by a factor of ${b}$ is $0.5$. 

Given ${a}$, ${b}$, and knowing that initially there is only a single cell of virus, calculate the expected number of virus cells after $\boldsymbol{\boldsymbol{t}}$ milliseconds. As this number can be very large, print your answer modulo $(10^9+7)$.

Input Format

A single line of three space-separated integers denoting the respective values of ${a}$ (the first growth factor), ${b}$ (the second growth factor), and ${t}}$ (the time you want to know the expected number of cells for).

Constraints

$1\leq t\leq10^{18}$  
$1\leq a,b\leq100$  
it is guaranteed that expected value is integer

Output Format

Print the expected number of virus cells after $\boldsymbol{\boldsymbol{t}}$ milliseconds modulo $(10^9+7)$.

Sample Input
2 4 1

Sample Output
3

Explanation

Initially, the virus has one cell. After a millisecond, with probability $0.5$, its size is doubled and, with probability of the other $0.5$ in the sample space, its size grows by ${4}$ times. Thus, the expected number of virus cell after ${1}$ millisecond is $0.5\cdot2\cdot1+0.5\cdot4\cdot1=3\%\ (10^9+7)=3$. Thus, we print $3$ on a new line.
"""

def expected_virus_cells(a: int, b: int, t: int) -> int:
    MOD = 10 ** 9 + 7
    D = (a + b) // 2
    R = 1
    while t > 0:
        if t % 2:
            R = R * D % MOD
        D = D * D % MOD
        t //= 2
    return R