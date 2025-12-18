"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Chef is playing a game with his brother Chefu. Before the game begins, C cards are placed on a table. Each card has a number written on it; since C can be very large, these numbers are described by two sequences A and D. Each of these sequences has length N; for each i (1 ≤ i ≤ N), D_{i} cards, each with number A_{i} written on it, are placed on the table. Therefore, C is equal to the sum of elements of D. Note that the elements of A don't have to be unique.

You are also given a sequence B with length K. The game will last for exactly K rounds numbered 1 through K. The players alternate turns — Chef plays on odd-numbered turns and his brother on even-numbered turns. In the i-th round, the current player must select B_{i} cards currently lying on the table, keep these cards on the table and discard all other cards.

Chef's goal is to maximize the sum of numbers written on cards that remain on the table after the last round, while Chefu's goal is minimize this sum. What will be the sum of numbers written on cards remaining on the table if both players play optimally?

------ Input ------ 

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A_{1}, A_{2}, ..., A_{N}.
The third line contains N space-separated integers D_{1}, D_{2}, ..., D_{N}.
The fourth line contains K space-separated integers B_{1}, B_{2}, ..., B_{K}.

------ Output ------ 

For each test case, print a single line containing one integer — the sum of numbers on cards that remain on the table at the end of the game.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N, K ≤ 100,000$
$1 ≤ sum of N over all test cases ≤ 100,000$
$1 ≤ sum of K over all test cases ≤ 100,000$
$1 ≤ A_{i}, D_{i} ≤ 1,000,000 for each valid i$
$1 ≤ B_{i} ≤ C for each valid i$
$B_{i+1} < B_{i} for each valid i$

------ Subtasks ------ 

Subtask #1 (20 points): 

$D_{i} = 1 for each valid i$
$sum of N over all test cases ≤ 1,000$
$sum of K over all test cases ≤ 1,000$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
1
4 2
1 2 3 4
2 2 2 2
6 3
----- Sample Output 1 ------ 
7
----- explanation 1 ------ 
Example case 1: The cards that are on table initially are 1, 1, 2, 2, 3, 3, 4, 4 Chef in his turn should select 6 cards to keep and discard the rest, so he will keep 2, 2,
3, 3, 4, 4 after that Chefu should keep 3 cards and discard the rest, so he will keep 2, 2,
3 after that the game ends and sum of cards remained on the table is 2 + 2 + 3 = 7
"""

def optimal_card_game_result(N, K, A, D, B):
    # Combine A and D into a list of tuples (value, count)
    cards = [(A[i], D[i]) for i in range(N)]
    
    # Sort cards by value
    cards.sort()
    
    # Calculate the initial total number of cards
    total_cards = sum(D)
    
    # Initialize the answer list with the initial total number of cards
    ans = [total_cards]
    
    # Simulate the game rounds
    for i in range(K):
        if i % 2 == 0:  # Chef's turn (maximize)
            ans.append(ans[-1] - B[i] + 1)
        else:  # Chefu's turn (minimize)
            ans.append(ans[-1] + B[i] - 1)
    
    # Determine the final number of cards to keep
    x = max(ans[-1], ans[-2])
    y = min(ans[-1], ans[-2])
    
    # Find the indices in the sorted cards list where the number of cards changes
    p = 0
    index1 = index2 = None
    for i in range(len(cards)):
        p += cards[i][1]
        if p >= y and index1 is None:
            index1 = i
            x1 = p - y + 1
        if p >= x:
            index2 = i
            x2 = x - p + cards[i][1]
            break
    
    # Calculate the final sum of the remaining cards
    if index1 == index2:
        v = cards[index1][0] * (x - y + 1)
    else:
        v = cards[index1][0] * x1 + cards[index2][0] * x2
        for i in range(index1 + 1, index2):
            v += cards[i][0] * cards[i][1]
    
    return v