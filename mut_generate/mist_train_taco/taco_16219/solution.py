"""
QUESTION:
A colored stripe is represented by a horizontal row of n square cells, each cell is pained one of k colors. Your task is to repaint the minimum number of cells so that no two neighbouring cells are of the same color. You can use any color from 1 to k to repaint the cells.

Input

The first input line contains two integers n and k (1 ≤ n ≤ 5·105; 2 ≤ k ≤ 26). The second line contains n uppercase English letters. Letter "A" stands for the first color, letter "B" stands for the second color and so on. The first k English letters may be used. Each letter represents the color of the corresponding cell of the stripe.

Output

Print a single integer — the required minimum number of repaintings. In the second line print any possible variant of the repainted stripe.

Examples

Input

6 3
ABBACC


Output

2
ABCACA


Input

3 2
BBB


Output

1
BAB
"""

def min_repaints_to_avoid_adjacent_colors(n, k, s):
    if k == 2:
        # Two possible patterns for k == 2
        sol1 = list(s)
        ans1 = 0
        for i in range(n):
            if i % 2 == 0 and sol1[i] == 'B':
                ans1 += 1
                sol1[i] = 'A'
            elif i % 2 != 0 and sol1[i] == 'A':
                ans1 += 1
                sol1[i] = 'B'
        
        sol2 = list(s)
        ans2 = 0
        for i in range(n):
            if i % 2 == 0 and sol2[i] == 'A':
                ans2 += 1
                sol2[i] = 'B'
            elif i % 2 != 0 and sol2[i] == 'B':
                ans2 += 1
                sol2[i] = 'A'
        
        if ans1 <= ans2:
            min_repaints = ans1
            repainted_stripe = ''.join(sol1)
        else:
            min_repaints = ans2
            repainted_stripe = ''.join(sol2)
    else:
        # General case for k > 2
        s = list(s)
        ans = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                ans += 1
                x = chr((ord(s[i - 1]) - 65 + 1) % k + 65)
                if i == n - 1 or s[i + 1] != x:
                    s[i] = x
                else:
                    y = chr((ord(s[i - 1]) - 65 + 2) % k + 65)
                    s[i] = y
        
        min_repaints = ans
        repainted_stripe = ''.join(s)
    
    return min_repaints, repainted_stripe