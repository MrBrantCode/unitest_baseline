"""
QUESTION:
After dating for a long time, Akhil is finally going to propose to his girlfriend. She is very strong in mathematics, and will accept his proposal, if and only if Akhil solves a problem given by her. The problem is given below. Help Akhil solve it.

Akhil is given two numbers N and M, and he has to tell her the remainder when $111\cdots(\text{N times})$ is divided by $\mbox{M}$.  

Input Format 

The first line contains an integer ${T}$ i.e. the number of test cases. 

Each of the next ${T}$ lines contain two space separated integers, $N$ and $\mbox{M}$.  

Output Format 

${T}$ lines each containing ouptut for the corresponding test case. 

Constraints 

$1\leq T\leq10001$ 

$1\leq N\leq10^{16}$ 

$2\leq M\leq10^{9}$  

Sample Input 00  

3
3 3
4 7
5 18

Sample Output 00  

0
5   
5

Explanation 

111 % 3  = 0 

  1111 % 7 = 5 

  11111%18 = 5
"""

def calculate_remainder(N, M):
    ans = pow(10, N, 9 * M)
    ans = (ans - 1) // 9
    return ans