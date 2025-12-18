"""
QUESTION:
Alice and Bob invented the following silly game:

The game starts with an integer, $n$, that's used to build a $\boldsymbol{set}$ of $n$ distinct integers in the inclusive range from $1$ to $n$ (i.e., $set=\{1,2,3,\ldots,n-1,n\}$).
Alice always plays first, and the two players move in alternating turns.
During each move, the current player chooses a prime number, $\boldsymbol{p}$, from $\boldsymbol{set}$. The player then removes $\boldsymbol{p}$ and all of its multiples from $\boldsymbol{set}$.
The first player to be unable to make a move loses the game.

Alice and Bob play $\mathrm{~g~}$ games. Given the value of $n$ for each game, print the name of the game's winner on a new line. If Alice wins, print Alice; otherwise, print Bob.

Note: Each player always plays optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.

Input Format

The first line contains an integer, $\mathrm{~g~}$, denoting the number of games Alice and Bob play. 

Each line $\boldsymbol{i}$ of the $\mathrm{~g~}$ subsequent lines contains a single integer, $n$, describing a game.

Constraints

$1\leq g\leq1000$  
$1\leq n\leq10^5$

Subtasks

$1\leq n\leq1000$ for $50\%$ of the maximum score

Output Format

For each game, print the name of the winner on a new line. If Alice wins, print Alice; otherwise, print Bob.

Sample Input 0
3
1
2
5

Sample Output 0
Bob
Alice
Alice

Explanation 0

Alice and Bob play the following $g=3$ games:

We are given $n=1$, so $set=\{1\}$. Because Alice has no valid moves (there are no prime numbers in the set), she loses the game. Thus, we print Bob on a new line.
We are given $n=2$, so $set=\{1,2\}$. Alice chooses the prime number $p=2$ and deletes it from the set, which becomes $set=\{1\}$. Because Bob has no valid moves (there are no prime numbers in the set), he loses the game. Thus, we print Alice on a new line.
We are given $n=5$, so $set=\{1,2,3,4,5\}$. Alice chooses the prime number $p=2$ and deletes the numbers $2$ and $4$ from the set, which becomes $set=\{1,3,5\}$. Now there are two primes left, $3$ and $5$. Bob can remove either prime from the set, and then Alice can remove the remaining prime. Because Bob is left without a final move, Alice will always win. Thus, we print Alice on a new line.
"""

def determine_game_winners(g: int, n_list: list) -> list:
    """
    Determines the winner of each game between Alice and Bob based on the given rules.

    Parameters:
    g (int): The number of games to be played.
    n_list (list): A list of integers where each integer represents the value of n for a game.

    Returns:
    list: A list of strings where each string indicates the winner of the corresponding game.
    """
    # Precompute the number of primes up to each number using the Sieve of Eratosthenes
    prime_pre = [0] * 100001
    sieve = [0] * 100001
    
    for i in range(2, 100000):
        if sieve[i] == 0:
            prime_pre[i] = prime_pre[i - 1] + 1
            for j in range(i, 100001, i):
                sieve[j] = i
        else:
            prime_pre[i] = prime_pre[i - 1]
    
    # Determine the winner for each game
    winners = []
    for n in n_list:
        winners.append('Bob' if prime_pre[n] % 2 == 0 else 'Alice')
    
    return winners