"""
QUESTION:
As punishment for attacking Sunland, Wet Shark is now forced to walk on a line of numbered squares, starting from $\mbox{1}$ and going to infinity. Wet Shark initially has a strength of $\mbox{S}$. To make the experience harder for Wet Shark, each square that has a label divisible by $\begin{array}{c}4\end{array}$ and/or $2$ but not divisible by $\textbf{42}$ contains a black glob of jelly, stepping on which his strength decreases by $\mbox{1}$. 

Wet Shark does not know that this line of squares is infinitely long, and he is determined to continue walking until his strength reaches $\mbox{0}$. Wet Shark walks from square to square, so he starts at square $\mbox{1}$, goes to square $2$, then $3$, then $\begin{array}{c}4\end{array}$, etc. 

Wet Shark’s punisher needs your help, and wants to compute where Wet Shark will stop in order to meet him there and punish him. Given Wet Shark’s initial strength $\mbox{S}$, find the square on which Wet Shark’s strength will reach $\mbox{0}$. Wet Shark can go far if defenses are not strong enough, so please output the answer modulo $10^9+7$. Wet Shark is curious, so he wants to know that given $\mbox{S}$ strength initially, how far he will go for different values $\mbox{S}$. Help him figure out how long he can go without doom for each $\mbox{S}$.

Input Format

The first line of the input contains an integer $\mathbf{T}$, the number of queries. The following lines describe the queries.

Each query consists of a line containing a single integer, which is the value of $\mbox{S}$.

Output Format

Print $\mathbf{T}$ lines, each line containing the answer for each query, i.e. the last square Wet Shark will reach before he runs out of strength, starting with a strength of $\mbox{S}$, modulo $10^9+7$.

Constraints  

$1\leq T\leq100$ 

$1\leq S\leq10^{18}$  

Sample Input
2
3
4

Sample Output
6 
8

Explanation

Square 1: 3 strength 

Square 2: 2 strength 

Square 3: 2 strength 

Square 4: 1 strength 

Square 5: 1 strength 

Square 6: 0 strength  

Thus the answer is 6.
"""

def calculate_last_square(S: int) -> int:
    MOD = 10**9 + 7
    twenties = S // 20
    rem = S % 20
    
    if rem == 0:
        return (42 * twenties - 2) % MOD
    else:
        return (42 * twenties + 2 * rem) % MOD