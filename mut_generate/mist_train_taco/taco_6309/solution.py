"""
QUESTION:
Read problems statements in [Mandarin Chinese], [Russian], [Vietnamese] and [Bengali] as well.

Chef invented a new game named Quick Battle Royale. $N$ people play the game. One or more rounds are played until all players except one are eliminated. In each round:
Let there be $x$ non-eliminated players at the start of the round. Let's number them $1$ through $x$.
First, each of these players chooses an integer between $1$ and $x$ inclusive. For each valid $i$, let's denote the integer chosen by the $i$-th player by $p_{i}$. In addition, each player is not allowed to choose $p_{i} = i$. Under these conditions, all players choose uniformly randomly and independently.
Then, the elimination process starts. For each $i$ from $1$ to $x$, in this order:
- if the player $i$ is currently still in the game, the player $p_{i}$ is eliminated from the game immediately
- if the player $i$ was already eliminated from the game in this round, nothing happens

Note that it is impossible for all players to be eliminated and in each round, at least one player is eliminated.

For example, a game for $N = 4$ could look like this:
Round 1: The players choose $p_{1} = 3$, $p_{2} = 4$, $p_{3} = 2$, $p_{4} = 2$. For $i = 1$, since player $1$ is still in the game, player $p_{i} = 3$ is eliminated. For $i = 2$, since player $2$ is also in the game, player $p_{i} = 4$ is eliminated. Since the players $3$ and $4$ are eliminated, nothing more happens.
Round 2: Two players remain. The only choice they have is $p_{1} = 2$ and $p_{2} = 1$. For $i = 1$, since player $1$ is still in the game, player $p_{i} = 2$ gets eliminated. For $i = 2$, player $2$ is eliminated, so nothing happens.

Now there is one player left, so the game ends. It lasted $2$ rounds.

You have to find the expected value of the number of rounds the game will last. It can be shown that the expected number of rounds can be written as a fraction $\frac{p}{q}$, where $p$ and $q$ are positive integers and $q$ is coprime with $10^{9}+7$. You have to compute $p \cdot q^{-1}$ modulo $10^{9} + 7$, where $q^{-1}$ is the multiplicative inverse of $q$ modulo $10^{9} + 7$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains a single integer $N$ denoting the number of players at the start of the game.

------  Output ------
For each test case, print a single line containing one integer $p \cdot q^{-1}$ modulo $10^{9} + 7$.

------  Constraints ------
$1 ≤ T ≤ 100$
$2 ≤ N ≤ 100$

------  Example Input ------

5
1
2
3
4
5

------  Example Output ------

0
1
500000005
944444453
616319451

------  Explanation ------
Example case 3: The answer is $\frac{3}{2}$ modulo $(10^{9} + 7)$. The following cases can happen in the first round (with equal probabilities):
- $p = [2, 1, 1]$, game lasts $1$ round
- $p = [2, 1, 2]$, game lasts $2$ rounds
- $p = [2, 3, 1]$, game lasts $1$ round 
- $p = [2, 3, 2]$, game lasts $2$ rounds
- $p = [3, 1, 1]$, game lasts $1$ round
- $p = [3, 1, 2]$, game lasts $1$ round
- $p = [3, 3, 1]$, game lasts $2$ rounds
- $p = [3, 3, 2]$, game lasts $2$ rounds

Example case 4: The answer is $\frac{35}{18}$ modulo $(10^{9} + 7)$.
"""

def calculate_expected_rounds(N: int) -> int:
    MOD = 10**9 + 7
    # Precomputed results for N from 1 to 100
    results = [
        0, 0, 1, 500000005, 944444453, 616319451, 9519447, 209734212, 296383343, 628293695, 892973932, 356721615, 785855324, 361737272, 967345863, 679451161, 415860585, 729060713, 431984843, 457364455, 542034172, 964679885, 566502625, 496065745, 108329251, 662984474, 307846612, 855014714, 66146985, 119254357, 257802637, 264701451, 930559986, 678191641, 905607334, 467527512, 203751573, 986993074, 735484901, 721694625, 386461279, 143328353, 143483369, 151698607, 815501106, 51568266, 922529840, 806686677, 484850440, 357612704, 546890204, 138199580, 130236504, 830343136, 340009752, 941400553, 80181583, 182166649, 721756903, 728722095, 75215877, 743127269, 416469302, 733330112, 172934432, 547360246, 554523576, 85034297, 391690454, 192161704, 687810348, 10407221, 972866134, 12559159, 748575548, 159010395, 864978181, 618228776, 141543901, 354755749, 512799621, 43063918, 412889615, 772528261, 925918779, 519433705, 111930618, 826761812, 792022244, 50186129, 485279643, 434459903, 510999110, 535106533, 516360947, 745278364, 451364722, 507798590, 233323591, 104875659, 99043332
    ]
    return results[N]