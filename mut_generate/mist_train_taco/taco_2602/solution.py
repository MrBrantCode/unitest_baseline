"""
QUESTION:
Chef loves games! But he likes to invent his own. Now he plays game "Digit Jump". Chef has a sequence of digits $S_{1}, S_{2}, \ldots , S_{N}$. He is staying in the first digit $S_{1}$ and wants to reach the last digit $S_{N}$ in the minimal number of jumps. 
While staying in some index $i$ Chef can jump into $i - 1$ and $i + 1$, but he can't jump out from sequence. Or he can jump into any digit with the same value $S_i$. 
Help Chef to find the minimal number of jumps he need to reach digit $S_{N}$ from digit $S_1$. 

-----Input-----
Input contains a single line consist of string $S$ of length $N$ - the sequence of digits.

-----Output-----
In a single line print single integer - the minimal number of jumps he needs.

-----Constraints-----
- $1\leq N \leq 10^5$
- Each symbol of $S$ is a digit from $0$ to $9$. 

-----Example Input 1-----
01234567890

-----Example Output 1-----
1

-----Example Input 2-----
012134444444443

-----Example Output 2-----
4

-----Explanation-----
Test Case 1: Chef can directly jump from the first digit (it is $0$) to the last (as it is also $0$).
Test Case 2: Chef should follow the following path: $1 - 2 - 4 - 5 - 15$.
"""

import heapq

def minimal_jumps_to_end(sequence):
    L = len(sequence)
    if L == 1 or L == 2:
        return L - 1
    
    numPos = [[] for _ in range(10)]
    minJump = [2000000 for _ in range(L)]
    minJump[L - 1] = 0
    maxJumpForNum = [2000000 for _ in range(10)]
    
    for i in range(L):
        numPos[int(sequence[i])].append(i)
    
    h = []
    heapq.heappush(h, (0, int(sequence[L - 1]), L - 1))
    
    while len(h) > 0:
        (minJ, num, idx) = heapq.heappop(h)
        setJump = minJ + 1
        
        if maxJumpForNum[num] > setJump:
            maxJumpForNum[num] = setJump
            for i in numPos[num]:
                if i == idx:
                    continue
                if minJump[i] > setJump:
                    minJump[i] = setJump
                    heapq.heappush(h, (setJump, num, i))
        
        if idx > 0:
            if minJump[idx - 1] > setJump:
                minJump[idx - 1] = setJump
                heapq.heappush(h, (setJump, int(sequence[idx - 1]), idx - 1))
        
        if idx < L - 2:
            if minJump[idx + 1] > setJump:
                minJump[idx + 1] = setJump
                heapq.heappush(h, (setJump, int(sequence[idx + 1]), idx + 1))
    
    return minJump[0]