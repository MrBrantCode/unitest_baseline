"""
QUESTION:
Given an array A of N integers. Two players play a game with the array in turns. The game aims to make the array equal. Players add 1 to any number of the array to increase it by 1(except the maximum number). The player who adds last i.e. the player after whose turn the array becomes equal is declared the winner. If no moves can be made, the game is a draw.
Example 1:
Input:
N=2
A[]={1,2}
Output:
First
Explanation:
The first player adds 1 to the first 
number making it 2. The array 
becomes equal, so he is the winner.
Example 2:
Input:
N=3
A[]={2,2,2}
Output:
Draw
Explanation:
No moves can be made as all the elements are
already maximum and numbers cannot be
added to the maximum numbers.
Your Task:
You don't need to read input or print anything. Your task is to complete the function arrayGame() which takes an integer N and an integer array A as input parameters and returns a string denoting the result of the game. ("Draw" if the game is a draw, "First" if the first player and "Second" otherwise).
Expected Time Complexity: O(N)
Expected Auxillary Space: O(1)
Constraints:
1<=N<=10^{6}
1<=A[i]<=10^{9}
"""

def determine_game_result(N, A):
    x = max(A)
    a = N * x
    c = sum(A) - a
    
    if a == sum(A):
        return 'Draw'
    if c % 2 == 0:
        return 'Second'
    else:
        return 'First'