"""
QUESTION:
Alice and Bob are playing a game. Alice goes first.

They have a binary circular array A with N elements. In one move, a player can:
Choose a *circular continuous segment* of the array and perform a *left cyclic shift* on the chosen segment.

We define the term diff(A) as the number of pairs of adjacent elements with different values.
Note that we also consider A_{N} and A_{1} as adjacent.

A player can make a move only if, for the updated array A', diff(A')> diff(A).

The player who is unable to make a move, loses. Find the winner of the game if both players play optimally.

Note:
For an array A with N elements, some *circular continuous segments* are [A_{1}], [A_{1}, A_{2}, A_{3}], [A_{N-1}, A_{N}, A_{1}, A_{2}], etc.
A *left cyclic shift* of a segment [A_{1}, A_{2}, A_{3}] is [A_{2}, A_{3}, A_{1}]. Similarly, *left cyclic shift* of segment [A_{N-1}, A_{N}, A_{1}, A_{2}] is [A_{N}, A_{1}, A_{2}, A_{N-1}].

------ Input Format ------ 

- The first line of input contains a single integer T, the number of test cases. The description of the test cases follows.
- Each test cases consists of two lines of input.
- The first line of each test case contains a single integer N, the number of elements.
- The second line of each test case contains N space-separated integers A_{1},A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, if Alice will win print Alice, otherwise print Bob.

You may print each character in Uppercase or Lowercase. For example: BOB, bob, boB, and Bob are all identical.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{6}$
$0 ≤ A_{i} ≤ 1$
- The sum of $N$ over all test cases won't exceed $10^{6}$.

------ subtasks ------ 

None

----- Sample Input 1 ------ 
3
3
1 0 1
4
1 1 0 0
8
1 0 1 0 0 0 1 1

----- Sample Output 1 ------ 
Bob
Alice
Bob
----- explanation 1 ------ 
Test case $1$: Alice can not perform any move. Thus, Bob wins.

Test case $2$: Alice can perform the following move:
- Choose the segment $[A_{1},A_{2},A_{3}]$ and perform *left cyclic shift*. Thus, $A$ becomes $[1,0,1,0]$.  
Also, $diff([1, 1, 0, 0]) = 2$ as pairs of adjacent elements with different values are $(A_{2}, A_{3})$ and $(A_{4}, A_{1})$. After this move, $diff([1, 0, 1, 0]) = 4$ as all pairs of adjacent elements have different values. Since $diff([1, 0, 1, 0]) > diff([1, 1, 0, 0])$, this move is valid.

After performing the move, Bob has no valid move left. Thus, Alice wins.
"""

def determine_winner(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        ones, zeros = 0, 0
        isone, iszero = False, False
        i = 1
        
        while i < N:
            if A[i] == 1:
                isone = True
            else:
                iszero = True
            tmp = 0
            if A[i] == A[i - 1]:
                while i < N and A[i] == A[i - 1]:
                    i += 1
                    tmp += 1
                i -= 1
                if A[i] == 0:
                    zeros += tmp
                else:
                    ones += tmp
            i += 1
        
        if N > 2 and A[0] == A[-1]:
            if A[0] == 1:
                ones += 1
            else:
                zeros += 1
        
        if ones == 0 or zeros == 0:
            results.append('Bob')
            continue
        
        if min(ones, zeros) % 2:
            results.append('Alice')
        else:
            results.append('Bob')
    
    return results