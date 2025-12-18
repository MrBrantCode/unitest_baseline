"""
QUESTION:
Animesh and Mohit are playing a game. They have $N$ balls in front of them. All the balls are numbered, not necessarily in any order. Animesh picks a set of ${K}$ balls from the lot each time, checks this set, puts it back into the lot, and repeats this process until all possible selections have been made. At each draw, Mohit picks two balls from these ${K}$ balls -- the one with the maximum number and the one with the minimum number, and notes their difference on a paper. At the end of the game, Animesh has to tell the $\textit{Sum}$ of all the numbers on Mohit's paper. As value of this number can be very huge, you have to tell the value mod $10^9+7$.  

Input Format 

The first line contains two integers $N$ and ${K}$. 

The next line will contain a list having $N$ numbers.  

Output Format 

Print the value of $\textit{Sum}$  mod $(10^9+7)$.  

Constraints 

$1\leq N\leq10^5$ 

$1\leq K\leq N$ 

$0\leq\:\text{numbers_on_ball}\:\leq10^9$  

Sample Input  

4 2
10 20 30 40

Sample Output  

100

Explanation

There are 6 possible selections. 

1. 10 20 

2. 20 30 

3. 30 40 

4. 10 30 

5. 20 40 

6. 10 40 

Summation = 10+10+10+20+20+30 = 100
"""

def calculate_sum_of_differences(N, K, balls):
    P = 10**9 + 7
    balls.sort()
    inv = [0, 1]
    
    for i in range(2, N + 1):
        inv.append(P - P // i * inv[P % i] % P)
    
    comb = 1
    ans = 0
    
    for pick in range(K - 1, N):
        ans += (balls[pick] - balls[N - 1 - pick]) * comb % P
        ans %= P
        comb = comb * (pick + 1) % P * inv[pick + 2 - K] % P
    
    return ans