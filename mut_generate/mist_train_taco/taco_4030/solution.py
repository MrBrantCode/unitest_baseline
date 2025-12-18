"""
QUESTION:
Everybody is sad, most of all Monica as Chandler must spend Christmas and New Years in Tulsa, where his staff is all depressed they can't be with their families. He arranged for the head office to send a bonus, but even that's another bummer: donations in their name to the New York ballet. Chandler sends a message to the head office in the form of a binary code, which somehow gets changed on the way.

Chef is given two binary strings S and T of lengths N and M respectively. We can perform the following operations on string S.

Select two adjacent characters of the string S and flip these two characters. ( Flipping the character 1 is equivalent to replacing the character 1 with 0, and vice-versa )
Add a character, either 0 or 1 to any of the ends ( either the front or the back ) of the string S.

Find the minimum number of operations needed to convert S to T. If it is impossible to convert S to T, print -1.

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- First line of each testcase contains of a single line of input, two integers N, M.
- Second line of each testcase contains a binary string S.
- Third line of each testcase contains a binary string T.

------ Output Format ------ 

For each testcase, output in a single line the minimum number of operations needed to convert S to T. If it is impossible to convert, print -1.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$1 ≤ N, M ≤ 1000$
$S, T$ contain $0, 1$ only.

----- Sample Input 1 ------ 
2
3 3
101
000
4 3
0100
000

----- Sample Output 1 ------ 
2
-1

----- explanation 1 ------ 
Test case 1: Flip the first two bits in one move and second two bits in second move. $101$ $\rightarrow$  $011$ $\rightarrow$ $000$.

Test case 2: It is impossible to convert $S$ to $T$ using any sequence of moves.
"""

def min_operations_to_convert_binary_strings(S, T):
    n = len(S)
    m = len(T)
    
    if m < n:
        return -1
    
    diff = m - n
    mn = float('inf')
    
    for i in range(diff + 1):
        seq = []
        if i != 0:
            seq.append(i - 1)
        else:
            seq.append(float('-inf'))
        
        for j in range(n):
            if S[j] != T[j + i]:
                seq.append(j + i)
        
        if diff - i != 0:
            seq.append(n + i)
        else:
            seq.append(float('inf'))
        
        if len(seq) == 2:
            return diff
        
        dp = [[float('inf'), float('inf')] for _ in range(len(seq) + 4)]
        dp[0][0] = 0
        dp[0][1] = 0
        
        j = 1
        while j < len(seq) - 1:
            dp[j][0] = min(dp[j][0], dp[j - 1][1] + seq[j] - seq[j - 1])
            dp[j][1] = dp[j - 1][0]
            j += 1
        
        mn = min(mn, diff + dp[len(seq) - 2][0], diff + dp[len(seq) - 2][1] + seq[len(seq) - 1] - seq[len(seq) - 2])
    
    if mn == float('inf'):
        return -1
    
    return mn