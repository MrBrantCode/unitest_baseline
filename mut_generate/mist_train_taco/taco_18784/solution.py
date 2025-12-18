"""
QUESTION:
D --Invisible

Problem Statement

You are trying to play a card game called "Invisible" with your friends. This card game uses two types of cards, a "scoring card" and a "jamming card". A positive value is written on each score card. The rules of this card game are as follows.

* The game is played by two players, player 1 and player 2. The game starts on player 1's turn.
* There is one stack and two decks in the field. The stack consists of cards placed by two players. In addition, the deck possessed by each player consists of the score card and the obstruction card possessed by that player. Players can check the order of cards in themselves or in their opponent's deck at any time. There are no cards on the stack at the beginning of the game.
* The two players alternately perform one of the following two actions exactly once.
* Put the top card of your deck on the top of the stack. However, this action cannot be performed when there are no cards in your deck.
* Pass your turn.
* When the player passes the turn, the following processing is performed.
* Each player gets all the scoring cards in the stack that meet the following two conditions. The score card obtained is removed from the field.
1. This is the score card you put on the stack.
2. Above any disturbing cards placed by your opponent (when there are no disturbing cards in your stack, the player gets all the cards he or she puts on the stack).
* Remove all cards in the stack.



If both players pass in succession with no cards on the stack, the game ends. The final score of each player is the sum of the numbers written on the score card obtained by each player.

Each player takes the best action to maximize the value obtained by subtracting the opponent's score from his own score. Your job is to calculate the difference between Player 1's score and Player 2's score when each player behaves optimally for each player's deck given.

Input

The input consists of a single test case of the form:

$ n $ $ m $
$ a_1 $ $ a_2 $ $ \ dots $ $ a_n $
$ b_1 $ $ b_2 $ $ \ dots $ $ b_m $

The first line consists of positive integers $ n $, $ m $ ($ 1 \ le n, m \ le 50 $) representing the number of decks. The second line consists of $ n $ integers, where $ a_i $ represents the $ i $ th card from the top of player 1's deck ($ 1 \ le i \ le n $). $ a_i $ is more than $ 1 $, less than $ 1 {,} 000 {,} 000 $, or $ -1 $. The third line consists of $ m $ integers, where $ b_j $ represents the $ j $ th card from the top of player 2's deck ($ 1 \ le j \ le m $). $ b_j $ is more than $ 1 $, less than $ 1 {,} 000 {,} 000 $, or $ -1 $. When $ a_i $ and $ b_j $ are positive integers, it represents a scoring card, and when it is $ -1 $, it represents a jamming card.

Output

Output (Score of Player 1)-(Score of Player 2) when each player behaves optimally.

Sample Input 1


twenty two
100 -1
200 300

Output for the Sample Input 1


-100

<image>
<image>
<image>


Sample Input 2


3 5
10 30 -1
-1 90 20 10 -1

Output for the Sample Input 2


0

Sample Input 3


4 5
15 20 10 30
50 30 10 20 25

Output for the Sample Input 3


-60





Example

Input

2 2
100 -1
200 300


Output

-100
"""

def calculate_score_difference(n, m, A, B):
    memo = dict()

    def dfs(a, b, skip, turn, a_stack, b_stack):
        key = (a, b, skip, turn, a_stack, b_stack)
        if key in memo:
            return memo[key]
        if skip == 3:
            return 0
        if turn % 2 == 0:
            memo[key] = dfs(a, b, skip + 1, (turn + 1) % 2, 0, 0) + a_stack - b_stack
            if len(A) == a:
                return memo[key]
            if A[a] == -1:
                b_stack = 0
            else:
                a_stack += A[a]
            memo[key] = max(memo[key], dfs(a + 1, b, 0, (turn + 1) % 2, a_stack, b_stack))
        else:
            memo[key] = dfs(a, b, skip + 1, (turn + 1) % 2, 0, 0) - b_stack + a_stack
            if len(B) == b:
                return memo[key]
            if B[b] == -1:
                a_stack = 0
            else:
                b_stack += B[b]
            memo[key] = min(memo[key], dfs(a, b + 1, 0, (turn + 1) % 2, a_stack, b_stack))
        return memo[key]

    return dfs(0, 0, 0, 0, 0, 0)