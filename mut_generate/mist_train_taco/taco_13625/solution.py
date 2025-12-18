"""
QUESTION:
One day Anna got the following task at school: to arrange several numbers in a circle so that any two neighboring numbers differs exactly by 1. Anna was given several numbers and arranged them in a circle to fulfill the task. Then she wanted to check if she had arranged the numbers correctly, but at this point her younger sister Maria came and shuffled all numbers. Anna got sick with anger but what's done is done and the results of her work had been destroyed. But please tell Anna: could she have hypothetically completed the task using all those given numbers?

Input

The first line contains an integer n — how many numbers Anna had (3 ≤ n ≤ 105). The next line contains those numbers, separated by a space. All numbers are integers and belong to the range from 1 to 109.

Output

Print the single line "YES" (without the quotes), if Anna could have completed the task correctly using all those numbers (using all of them is necessary). If Anna couldn't have fulfilled the task, no matter how hard she would try, print "NO" (without the quotes).

Examples

Input

4
1 2 3 2


Output

YES


Input

6
1 1 2 2 2 3


Output

YES


Input

6
2 4 1 1 2 2


Output

NO
"""

def can_arrange_in_circle(n, numbers):
    if n < 3:
        return "NO"
    
    g = {}
    for num in numbers:
        g[num] = g.get(num, 0) + 2
    
    mx = max(g)
    
    for i in sorted(g)[:-1]:
        if i + 1 not in g:
            return "NO"
        g[i + 1] -= g[i]
        if g[i + 1] < 0:
            return "NO"
    
    return "YES" if g[mx] == 0 and list(g.values()).count(0) == 1 else "NO"