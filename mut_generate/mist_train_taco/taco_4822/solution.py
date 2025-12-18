"""
QUESTION:
One of the oddest traditions of the town of Gameston may be that even the town mayor of the next term is chosen according to the result of a game. When the expiration of the term of the mayor approaches, at least three candidates, including the mayor of the time, play a game of pebbles, and the winner will be the next mayor.

The rule of the game of pebbles is as follows. In what follows, n is the number of participating candidates.

Requisites     A round table, a bowl, and plenty of pebbles. Start of the Game      A number of pebbles are put into the bowl; the number is decided by the Administration Commission using some secret stochastic process. All the candidates, numbered from 0 to n-1 sit around the round table, in a counterclockwise order. Initially, the bowl is handed to the serving mayor at the time, who is numbered 0. Game Steps      When a candidate is handed the bowl and if any pebbles are in it, one pebble is taken out of the bowl and is kept, together with those already at hand, if any. If no pebbles are left in the bowl, the candidate puts all the kept pebbles, if any, into the bowl. Then, in either case, the bowl is handed to the next candidate to the right. This step is repeated until the winner is decided. End of the Game      When a candidate takes the last pebble in the bowl, and no other candidates keep any pebbles, the game ends and that candidate with all the pebbles is the winner.

A math teacher of Gameston High, through his analysis, concluded that this game will always end within a finite number of steps, although the number of required steps can be very large.

Input

The input is a sequence of datasets. Each dataset is a line containing two integers n and p separated by a single space. The integer n is the number of the candidates including the current mayor, and the integer p is the total number of the pebbles initially put in the bowl. You may assume 3 ≤ n ≤ 50 and 2 ≤ p ≤ 50.

With the settings given in the input datasets, the game will end within 1000000 (one million) steps.

The end of the input is indicated by a line containing two zeros separated by a single space.

Output

The output should be composed of lines corresponding to input datasets in the same order, each line of which containing the candidate number of the winner. No other characters should appear in the output.

Sample Input


3 2
3 3
3 50
10 29
31 32
50 2
50 50
0 0


Output for the Sample Input


1
0
1
5
30
1
13






Example

Input

3 2
3 3
3 50
10 29
31 32
50 2
50 50
0 0


Output

1
0
1
5
30
1
13
"""

def determine_mayor_winner(n, p):
    # Initialize the list to keep track of pebbles each candidate has
    lst = [0] * n
    # Index of the current candidate holding the bowl
    ind = 0
    # Number of pebbles remaining in the bowl
    rest = p
    
    while True:
        if rest == 0:
            # If the bowl is empty, refill it with the pebbles the current candidate has
            rest = lst[ind]
            lst[ind] = 0
        else:
            # If the bowl has pebbles, take one and add it to the current candidate's count
            lst[ind] += 1
            rest -= 1
            # Check if the current candidate has all the pebbles
            if lst[ind] == p:
                return ind
        # Move to the next candidate in a counterclockwise order
        ind = (ind + 1) % n