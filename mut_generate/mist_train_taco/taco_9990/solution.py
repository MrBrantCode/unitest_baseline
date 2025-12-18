"""
QUESTION:
Alice and Bob are playing a game. They are given an array $A$ of length $N$. The array consists of integers. They are building a sequence together. In the beginning, the sequence is empty. In one turn a player can remove a number from the left or right side of the array and append it to the sequence. The rule is that the sequence they are building must be strictly increasing. The winner is the player that makes the last move. Alice is playing first. Given the starting array, under the assumption that they both play optimally, who wins the game?


-----Input-----

The first line contains one integer $N$ ($1 \leq N \leq 2*10^5$) - the length of the array $A$.

The second line contains $N$ integers $A_1$, $A_2$,...,$A_N$ ($0 \leq A_i \leq 10^9$)


-----Output-----

The first and only line of output consists of one string, the name of the winner. If Alice won, print "Alice", otherwise, print "Bob".


-----Examples-----

Input
1
5
Output
Alice
Input
3
5 4 5
Output
Alice
Input
6
5 8 2 1 10 9
Output
Bob


-----Note-----

None
"""

def determine_winner(N, A):
    l, r = 0, N - 1
    
    # Move the left pointer to the right until the sequence is no longer strictly increasing
    while l + 1 < N and A[l] < A[l + 1]:
        l += 1
    
    # Move the right pointer to the left until the sequence is no longer strictly increasing
    while r >= 0 and A[r] < A[r - 1]:
        r -= 1
    
    # Adjust the pointers to count the number of elements that can be taken
    l = l + 1
    r = N - r
    
    # Determine the winner based on the parity of the counts
    if l % 2 or r % 2:
        return 'Alice'
    else:
        return 'Bob'