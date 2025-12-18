"""
QUESTION:
A telephone number is a sequence of exactly $11$ digits such that its first digit is 8.

Vasya and Petya are playing a game. Initially they have a string $s$ of length $n$ ($n$ is odd) consisting of digits. Vasya makes the first move, then players alternate turns. In one move the player must choose a character and erase it from the current string. For example, if the current string 1121, after the player's move it may be 112, 111 or 121. The game ends when the length of string $s$ becomes 11. If the resulting string is a telephone number, Vasya wins, otherwise Petya wins.

You have to determine if Vasya has a winning strategy (that is, if Vasya can win the game no matter which characters Petya chooses during his moves).


-----Input-----

The first line contains one integer $n$ ($13 \le n < 10^5$, $n$ is odd) — the length of string $s$.

The second line contains the string $s$ ($|s| = n$) consisting only of decimal digits.


-----Output-----

If Vasya has a strategy that guarantees him victory, print YES.

Otherwise print NO.


-----Examples-----
Input
13
8380011223344

Output
YES

Input
15
807345619350641

Output
NO



-----Note-----

In the first example Vasya needs to erase the second character. Then Petya cannot erase a character from the remaining string 880011223344 so that it does not become a telephone number.

In the second example after Vasya's turn Petya can erase one character character 8. The resulting string can't be a telephone number, because there is no digit 8 at all.
"""

def has_vasya_winning_strategy(n, s):
    moves = n - 11
    if moves % 2 != 0:
        petya = (moves - 1) // 2
    else:
        petya = moves // 2
    
    cnt = 0
    arr = []
    for i in range(n):
        if s[i] == '8':
            arr.append(i)
            cnt += 1
    
    if cnt <= petya:
        return False
    
    moves -= petya
    if arr[petya] - petya <= moves:
        return True
    else:
        return False