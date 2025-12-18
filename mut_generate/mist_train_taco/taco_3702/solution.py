"""
QUESTION:
Akash and Akhil are playing a game. They have $N$ balls numbered from $0$ to $N-1$. Akhil asks Akash to reverse the position of the balls, i.e., to change the order from say, 0,1,2,3 to 3,2,1,0. He further asks Akash to reverse the position of the balls $N$ times, each time starting from one position further to the right, till he reaches the last ball. So, Akash has to reverse the positions of the ball starting from ${0}^{t h}$ position, then from $1^{st}$ position, then from $2^{nd}$ position and so on. At the end of the game, Akhil will ask Akash the final position of any ball numbered $\mbox{K}$. Akash will win the game, if he can answer. Help Akash.

Input Format 

The first line contains an integer $\mathbf{T}$, i.e., the number of the test cases. 

The next $\mathbf{T}$ lines will contain two integers $N$ and $\mbox{K}$. 

Output Format 

Print the final index of ball $\mbox{K}$ in the array.  

Constraints 

$1\leq T\leq50$ 

$1\leq N\leq10^5$ 

$0\leq K\lt N$

Sample Input  

2
3 1
5 2

Sample Output  

2
4

Explanation 

For first test case, The rotation will be like this: 

0 1 2 -> 2 1 0 -> 2 0 1 -> 2 0 1

So, Index of 1 will be 2.
"""

def final_position_of_ball(N, K):
    for i in range(0, N):
        if K >= i:
            K = i + N - 1 - K
    return K