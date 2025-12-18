"""
QUESTION:
Koga and Ryuho, new generation Athena's saints, are training to improve their control over the cosmos. According to the ancient Masters, a saint's power to control the cosmos strengthens, when one allows the energy of the universe to flow within the body and then concentrates it. This energy can even be used to explode the objects. 

Today's training is based on a game, and the goal is to use as little cosmos as possible to win. Two saints play as follows: 

Initially there are $N$ piles of stones; pile $\mbox{1}$ has $\mbox{1}$ stone, pile $2$ has $2$ stones, and so on. Thus, the $i^{\mbox{th}}$ pile has $\boldsymbol{i}$ stones. The saints take turns and in each turn, a saint must select a non-empty pile and destroy at least half of the stones in it. The winner is the saint who destroys the last available stone . 

For example, from a pile of $7$ stones, a saint must destroy at least $\begin{array}{c}4\end{array}$ stones, leaving a single (and possibly empty) pile at most 3 stones. With such game, saints learn how to use the appropriate amount of cosmos in a single strike: too much will destroy more stones than desired, too little won't be enough. They also improve their battle thinking and strategy skills.

Ryuho suspects that such game is not as random as it appears to be at first glance. He strongly believes that with the correct single blow, you're assured to win from the very first turn, if you play optimally, no matter how good the other saint plays. Moreover, he is particularly interested in knowing the minimum number of stones he needs to destroy at that first move. Can you help him?  

Input Format

First line of the input consists of an integer $\mathbf{T}$, $\mathbf{T}$ testcases follow, each in a new line. Each line will contain a single integer $N$, which describes the number of initial piles as explained above.

Constraints

$1<=T<=10^6$  
$1<=N<=10^9$

Output Format

For each line in the input, output the minimum number of stones Ryuho needs to destroy in his first turn, assuming he starts playing and that both he and Koga play always as well as possible. If this is not possible, just print $\mbox{0}$.

Sample Input 0
5
1
10
6
8
123456

Sample Output 0
1
7
2
7
32768

Explanation 0

For the first testcase, we can see that the saint can destroy the first stone and win the game. 

Sample Input 1
1
3

Sample Output 1
1

Explanation 1

There are three piles with stones $1,2$ and $3$.
Initially Ryuho will remove $\mbox{1}$ stone from the first pile.
Now other saint has $\begin{array}{c}4\end{array}$ options - 

First, to remove all stones from second pile. In that case Ryuho will remove all stones from third pile and win the game.

Second, to remove all stones from third pile. In that case Ryuho will remove all stones from second pile and win the game.

Third, to remove $\mbox{1}$ stone from second pile. In that case Ryuho will remove $2$ stones from third pile and they will be left with $\mbox{1}$ stone in each of the second and third pile. No matter what the other saint selects Ryuho will have an option to select the last stone.

Fourth, to remove $2$ stones from the third pile. In that case Ryuho will remove $\mbox{1}$ stone from second pile and they will be left with $\mbox{1}$ stone in each of the second and third pile. No matter what the other saint selects Ryuho will have an option to select the last stone.

So in all four cases Ryuho will win the game.
"""

def calculate_min_stones_to_destroy(N):
    if N == 1 or N % 2 == 1:
        return 1
    
    (p, log) = (1, 1)
    while p * 2 <= N:
        p *= 2
        log += 1
    
    xor = log ^ 1
    ans = N + 1
    
    for prev in range(2, log + 1):
        need = prev ^ xor
        if need < prev:
            before = 1 << prev - 1
            after = (1 << need) - 1
            ans = min(ans, max(before - after, before // 2))
    
    return ans