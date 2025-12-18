"""
QUESTION:
Manasa loves the nim game, in which there are $n$ buckets, each having $A_i$ balls. Two players play alternately. Each turn consists of removing some non-zero number of balls from one of the bucket. A player with lack of moves looses. But, Manasa having played it so many times, she gets bored one day. So she wants to change the rules of the game. She loves prime numbers, so she makes a new rule: any player can only remove a prime number of balls from a bucket. But there are infinite number prime numbers. So to keep the game simple, a player can only remove $\boldsymbol{x}$ balls from a bucket if $\boldsymbol{x}$ belongs to the set $S=\{2,3,5,7,11,13\}.$

The whole game can now be described as follows:   

There are $n$ buckets, and the $k^{\text{th}}$ bucket contains $A_{k}$ balls. A player can choose a bucket and remove $\boldsymbol{x}$ balls from that bucket where $\boldsymbol{x}$ belongs to $\mbox{S}$. A player loses if there are no more available moves.

Manasa plays the first move against Sandy. Who will win if both of them play optimally?

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each test case consists of two lines. The first line contains a single integer $n$. The second line contain $n$ space-separated integers $A_{1},A_{2},\ldots,A_{n}$.  

Constraints

$1\leq t\leq10$  
$1\leq n\leq10^4$  
$1\leq A_k\leq10^{18}$  

Output Format

Print a single line containing the name of the winner: Manasa or Sandy.

Sample Input 0
2
2
10 10
3
2 2 3

Sample Output 0
Sandy
Manasa

Explanation 0

For the first testcase: Since both the buckets have same number of balls, Manasa can choose any one of them for her first move. If Manasa selects to remove $2,3,5$ or $7$ balls to remove from first bucket. Now, Sandy  can always counter her move by removing $7,7,5,3$ balls from first bucket if it's left with $8,7,5,3$ balls respectively. Now, there are no valid moves left for first bucket. The same thing repeats for second bucket and Sandy wins.

For the second testcase: Manasa removes $3$ balls from the third bucket. Now, if Sandy choose the remove $2$ balls from second bucket Manasa will empty the first bucket and if Sandy choose the remove $2$ balls from first bucket, Manasa will empty second one. Hence, Manasa wins.
"""

def determine_winner(test_cases):
    results = []
    for sizes in test_cases:
        nim = 0
        for size in sizes:
            nim ^= size % 9 // 2
        results.append('Manasa' if nim != 0 else 'Sandy')
    return results