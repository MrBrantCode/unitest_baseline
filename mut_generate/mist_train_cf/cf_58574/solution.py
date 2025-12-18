"""
QUESTION:
Write a function `numberOfMatches(n)` that takes an integer `n` representing the number of teams in a tournament and returns a list containing two integers: the total number of matches played and the total number of rounds played in the tournament until a winner is decided. The tournament rules are as follows: 
- If the current number of teams is even, each team gets paired with another team. A total of `n / 2` matches are played, and `n / 2` teams advance to the next round.
- If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams advance to the next round. 
The function should work for `1 <= n <= 10^6`.
"""

def numberOfMatches(n):
    matches = n - 1
    rounds = int(math.log(n, 2)) + (n != 2**int(math.log(n, 2)))
    return [matches, rounds]