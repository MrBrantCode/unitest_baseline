"""
QUESTION:
JJ found a balanced parenthesis sequence. He does not like balanced parentheses so he will make the parenthesis sequence unbalanced by swapping adjacent characters in the sequence. 

JJ is lazy and wants to know minimum number of adjacent swaps required to make the given balanced parenthesis sequence unbalanced.

A parenthesis sequence is called balanced if one can turn it into a valid mathematical expression by adding characters + and 1. Sequences such as (())() and ()() are balanced whereas sequences such as ())( and )() are unbalanced.   

------ Input Format ------ 

- The first line contains T - the number of test cases. Then the test cases follow.
- The first line of each test case contains S - a balanced parenthesis sequence.

------ Output Format ------ 

For each test case, output the minimum number of adjacent swaps required to make the parenthesis sequence unbalanced.

------ Constraints ------ 

$1 ≤ T ≤ 5\cdot10^{4}$
$2 ≤ |S| ≤ 10^{5}$
- Sum of $S$ does not exceeds $10^{6}$ over all test cases
$S$ is a balanced parentheses sequence

----- Sample Input 1 ------ 
4
()
(())
()()
((()))(())

----- Sample Output 1 ------ 
1
2
1
2

----- explanation 1 ------ 
- Test case $1$: Swap the first and second character to get the unbalanced sequence )(.
- Test case $2$: Swap the second and third character first to obtain the bracket sequence ()(). Now you can swap the first and second character to obtain the sequence )(() which is unbalanced.
"""

def min_swaps_to_unbalance(S: str) -> int:
    n = len(S)
    dist = []
    for i in range(n):
        if S[i] == ')':
            dist.append(i + 1)
    prefix = [0]
    for i in range(len(dist)):
        prefix.append(prefix[-1] + dist[i])
    dist = dist[::-1]
    
    def answer():
        ans = float('inf')
        (o, c, ind) = (0, 0, 0)
        for i in range(n):
            req = o - c + 1
            while dist[-1] < i + 1:
                dist.pop()
                ind += 1
            if n // 2 - ind < req:
                break
            cal = prefix[ind + req] - prefix[ind] - req * i - req * (req + 1) // 2
            ans = min(ans, cal)
            if S[i] == '(':
                o += 1
            else:
                c += 1
        return ans
    
    return answer()