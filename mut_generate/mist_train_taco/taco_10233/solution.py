"""
QUESTION:
Given an array arr of non-negative integers of size N, 2 players are playing a game. In each move, a player chooses an element from either end of the array, and the size of the array shrinks by one. Both players take alternate chances and the game continues until the size of the array becomes 0. Every time a player chooses an array element the array value is added to the player's score. At the end player with maximum score wins.
If player 1 starts the game, you have to predict whether player 1 will win the game or not. Both players will play optimally.
 
Example 1:
Input:
N = 3
arr[] = {2,6,3}
Output:
0 
Explanation:
Initially, player 1 can choose between 2 and 3. 
If he chooses 3 (or 2), then player 2 can choose 
from 2 (or 3) and 6. If player 2 chooses 6,
then player 1 will be left with 2 (or 3). 
So, final score of player 1 is 2 + 3 = 5,
and player 2 is 6. 
Hence, player 1 will never be the winner and 
output is 0.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function is1winner() which takes the array arr[], its size N and returns true if player 1 is the winner and false otherwise.
The driver code itself prints 1 if returned value is true and 0 otherwise.
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 1000
0<= arr[i] <= 10^{5}
"""

def is_player1_winner(arr, N):
    dp = [[-1 for _ in range(N)] for _ in range(N)]

    def playGame(l, r):
        if l > r:
            return 0
        if l == r:
            return arr[r]
        if dp[l][r] != -1:
            return dp[l][r]
        option1 = arr[l] + min(playGame(l + 2, r), playGame(l + 1, r - 1))
        option2 = arr[r] + min(playGame(l + 1, r - 1), playGame(l, r - 2))
        dp[l][r] = max(option1, option2)
        return dp[l][r]
    
    ans = playGame(0, N - 1)
    return ans > sum(arr) / 2