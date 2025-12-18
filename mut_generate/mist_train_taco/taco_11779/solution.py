"""
QUESTION:
You can't possibly imagine how cold our friends are this winter in Nvodsk! Two of them play the following game to warm up: initially a piece of paper has an integer q. During a move a player should write any integer number that is a non-trivial divisor of the last written number. Then he should run this number of circles around the hotel. Let us remind you that a number's divisor is called non-trivial if it is different from one and from the divided number itself. 

The first person who can't make a move wins as he continues to lie in his warm bed under three blankets while the other one keeps running. Determine which player wins considering that both players play optimally. If the first player wins, print any winning first move.

Input

The first line contains the only integer q (1 ≤ q ≤ 1013).

Please do not use the %lld specificator to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specificator.

Output

In the first line print the number of the winning player (1 or 2). If the first player wins then the second line should contain another integer — his first move (if the first player can't even make the first move, print 0). If there are multiple solutions, print any of them.

Examples

Input

6


Output

2


Input

30


Output

1
6


Input

1


Output

1
0

Note

Number 6 has only two non-trivial divisors: 2 and 3. It is impossible to make a move after the numbers 2 and 3 are written, so both of them are winning, thus, number 6 is the losing number. A player can make a move and write number 6 after number 30; 6, as we know, is a losing number. Thus, this move will bring us the victory.
"""

def determine_winner_and_move(q: int) -> tuple:
    if q == 1:
        return (1, 0)
    
    arr = []
    p = q
    
    # Factor out all 2's
    while p % 2 == 0:
        arr.append(2)
        p = p // 2
    
    # Check for odd factors
    x = int(p ** 0.5) + 1
    for i in range(3, x, 2):
        while p % i == 0:
            arr.append(i)
            p = p // i
    
    # If p is still greater than 2, then it is a prime factor
    if p > 2:
        arr.append(p)
    
    # Determine the winner and the first move
    if len(arr) == 1:
        return (1, 0)
    elif len(arr) == 2:
        return (2, 0)
    else:
        first_move = arr[0] * arr[1]
        return (1, first_move)