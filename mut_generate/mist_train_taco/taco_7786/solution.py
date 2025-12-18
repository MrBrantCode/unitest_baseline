"""
QUESTION:
Andy wants to play a game with his little brother, Bob.  The game starts with an array of distinct integers and the rules are as follows:

Bob always plays first.   
In a single move, a player chooses the maximum element in the array.  He removes it and all elements to its right. For example, if the starting array $arr=[2,3,5,4,1]$, then it becomes $ar r'=[2,3]$ after removing $[5,4,1]$.  
The two players alternate turns. 
The last player who can make a move wins.  

Andy and Bob play $\mathrm{~g~}$ games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

To continue the example above, in the next move Andy will remove $3$.  Bob will then remove $2$ and win because there are no more integers to remove.  

Function Description  

Complete the gamingArray function in the editor below.  

gamingArray has the following parameter(s):  

int arr[n]: an array of integers   

Returns 

- string: either ANDY or BOB  

Input Format

The first line contains a single integer $\mathrm{~g~}$, the number of games.

Each of the next $\mathrm{~g~}$ pairs of lines is as follows:

The first line contains a single integer, $n$, the number of elements in $\textbf{arr}$.
The second line contains $n$ distinct space-separated integers $arr\left[i\right]$ where $0\leq i<n$.  

Constraints

Array $\textbf{arr}$ contains $n$ distinct integers.

For $35\%$ of the maximum score:

$1\leq g\leq10$  
$1\leq n\leq1000$  
$1\leq ar r[i]\leq10^5$    
The sum of $n$ over all games does not exceed $\textbf{1000}$.

For $\textbf{100\%}$ of the maximum score:

$1\leq g\leq100$  
$1\leq n\leq10^5$  
$1\leq a_i\leq10^9$  
The sum of $n$ over all games does not exceed $10^{5}$.

Sample Input 0
2
5
5 2 6 3 4
2
3 1

Sample Output 0
ANDY
BOB

Explanation 0

Andy and Bob play the following two games:

Initially, the array looks like this: 

In the first move, Bob removes $\boldsymbol{6}$ and all the elements to its right, resulting in $A=[5,2]$: 

In the second move, Andy removes $5$ and all the elements to its right, resulting in $A=\left[\right]$: 

At this point, the array is empty and Bob cannot make any more moves. This means Andy wins, so we print ANDY on a new line.

In the first move, Bob removes $3$ and all the elements to its right, resulting in $A=\left[\right]$. As there are no elements left in the array for Andy to make a move, Bob wins and we print BOB on a new line.

Sample Input 1
2
5
1 3 5 7 9
5
7 4 6 5 9

Sample Output 1
BOB
ANDY

Explanation 1

In the first test, they alternate choosing the rightmost element until the end.  Bob, Andy, Bob, Andy, Bob.  

In the second case, Bob takes $\mbox{9}$, Andy takes $[7,4,6,5]$.
"""

def gamingArray(arr):
    # Sort the indices of the array based on the values in descending order
    idx_sorted = [x for (x, y) in sorted(enumerate(arr), key=lambda x: -x[1])]
    
    # Initialize the maximum index to the length of the array
    max_idx = len(arr)
    
    # Initialize the flag to determine if Bob wins
    bob_wins = False
    
    # Iterate through the sorted indices
    for i in range(len(arr)):
        idx = idx_sorted[i]
        if idx < max_idx:
            max_idx = idx
            bob_wins = not bob_wins
    
    # Return the winner based on the flag
    return 'BOB' if bob_wins else 'ANDY'