"""
QUESTION:
Tak has N cards. On the i-th (1 \leq i \leq N) card is written an integer x_i.
He is selecting one or more cards from these N cards, so that the average of the integers written on the selected cards is exactly A.
In how many ways can he make his selection?

-----Constraints-----
 - 1 \leq N \leq 50
 - 1 \leq A \leq 50
 - 1 \leq x_i \leq 50
 - N,\,A,\,x_i are integers.

-----Partial Score-----
 - 200 points will be awarded for passing the test set satisfying 1 \leq N \leq 16.

-----Input-----
The input is given from Standard Input in the following format:
N A
x_1 x_2 ... x_N

-----Output-----
Print the number of ways to select cards such that the average of the written integers is exactly A.

-----Sample Input-----
4 8
7 9 8 9

-----Sample Output-----
5

 - The following are the 5 ways to select cards such that the average is 8:
 - Select the 3-rd card.
 - Select the 1-st and 2-nd cards.
 - Select the 1-st and 4-th cards.
 - Select the 1-st, 2-nd and 3-rd cards.
 - Select the 1-st, 3-rd and 4-th cards.
"""

def count_ways_to_select_cards(N, A, x):
    # Adjust the values of x to be relative to the target average A
    x = [i - A for i in x]
    
    # Initialize the dp array
    dp = [[0 for _ in range(4901)] for _ in range(N)]
    dp[0][2450] += 1  # There's one way to select no cards
    if x[0] + 2450 >= 0 and x[0] + 2450 < 4901:
        dp[0][x[0] + 2450] += 1  # There's one way to select the first card if it's within bounds
    
    # Fill the dp array
    for i in range(1, N):
        for j in range(4901):
            dp[i][j] = dp[i - 1][j]
            if 0 <= j - x[i] < 4901:
                dp[i][j] += dp[i - 1][j - x[i]]
    
    # The answer is the number of ways to get an average of A, minus the one way to select no cards
    return dp[N - 1][2450] - 1