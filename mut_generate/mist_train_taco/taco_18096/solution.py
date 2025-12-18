"""
QUESTION:
In the game of Mastermind, there are two players — Alice and Bob. Alice has a secret code, which Bob tries to guess. Here, a code is defined as a sequence of n colors. There are exactly n+1 colors in the entire universe, numbered from 1 to n+1 inclusive.

When Bob guesses a code, Alice tells him some information about how good of a guess it is, in the form of two integers x and y.

The first integer x is the number of indices where Bob's guess correctly matches Alice's code. The second integer y is the size of the intersection of the two codes as multisets. That is, if Bob were to change the order of the colors in his guess, y is the maximum number of indices he could get correct.

For example, suppose n=5, Alice's code is [3,1,6,1,2], and Bob's guess is [3,1,1,2,5]. At indices 1 and 2 colors are equal, while in the other indices they are not equal. So x=2. And the two codes have the four colors 1,1,2,3 in common, so y=4.

<image> Solid lines denote a matched color for the same index. Dashed lines denote a matched color at a different index. x is the number of solid lines, and y is the total number of lines. 

You are given Bob's guess and two values x and y. Can you find one possibility of Alice's code so that the values of x and y are correct?

Input

The first line contains a single integer t (1≤ t≤ 1000) — the number of test cases. Next 2t lines contain descriptions of test cases.

The first line of each test case contains three integers n,x,y (1≤ n≤ 10^5, 0≤ x≤ y≤ n) — the length of the codes, and two values Alice responds with.

The second line of each test case contains n integers b_1,…,b_n (1≤ b_i≤ n+1) — Bob's guess, where b_i is the i-th color of the guess.

It is guaranteed that the sum of n across all test cases does not exceed 10^5.

Output

For each test case, on the first line, output "YES" if there is a solution, or "NO" if there is no possible secret code consistent with the described situation. You can print each character in any case (upper or lower).

If the answer is "YES", on the next line output n integers a_1,…,a_n (1≤ a_i≤ n+1) — Alice's secret code, where a_i is the i-th color of the code.

If there are multiple solutions, output any.

Example

Input


7
5 2 4
3 1 1 2 5
5 3 4
1 1 2 1 2
4 0 4
5 5 3 3
4 1 4
2 3 2 3
6 1 2
3 2 1 1 1 1
6 2 4
3 3 2 1 1 1
6 2 6
1 1 3 2 1 1


Output


YES
3 1 6 1 2
YES
3 1 1 1 2
YES
3 3 5 5
NO
YES
4 4 4 4 3 1
YES
3 1 3 1 7 7
YES
2 3 1 1 1 1

Note

The first test case is described in the statement.

In the second test case, x=3 because the colors are equal at indices 2,4,5. And y=4 because they share the colors 1,1,1,2.

In the third test case, x=0 because there is no index where the colors are the same. But y=4 because they share the colors 3,3,5,5.

In the fourth test case, it can be proved that no solution exists.
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush

def find_possible_code(n, x, y, guess):
    d = defaultdict(list)
    for i, color in enumerate(guess):
        d[color].append(i)
    
    for i in range(1, n + 2):
        e = str(i)
        if e not in d:
            break
    
    q = [(-len(d[color]), color) for color in d.keys()]
    heapify(q)
    
    ans = [0] * n
    for i in range(x):
        l, color = heappop(q)
        ans[d[color].pop()] = color
        l += 1
        if l:
            heappush(q, (l, color))
    
    p = []
    while q:
        l, color = heappop(q)
        p.extend(d[color])
    
    if p:
        h = (n - x) // 2
        y = n - y
        q = p[h:] + p[:h]
        for i, j in zip(p, q):
            if guess[i] == guess[j]:
                if y:
                    ans[i] = e
                    y -= 1
                else:
                    return False, None
            else:
                ans[i] = guess[j]
        
        for i in range(n - x):
            if y and ans[p[i]] != e:
                ans[p[i]] = e
                y -= 1
    
    return True, ans