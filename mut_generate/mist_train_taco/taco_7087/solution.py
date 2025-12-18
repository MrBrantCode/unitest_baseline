"""
QUESTION:
Johnny, like every mathematician, has his favorite sequence of distinct natural numbers.  Let’s call this sequence $\mbox{M}$. Johnny was very bored, so he wrote down $N$ copies of the sequence $\mbox{M}$ in his big notebook. One day, when Johnny was out, his little sister Mary erased some numbers(possibly zero) from every copy of $\mbox{M}$ and then threw the notebook out onto the street. You just found it. Can you reconstruct the sequence? 

In the input there are $N$ sequences of natural numbers representing the $N$ copies of the sequence $\mbox{M}$ after Mary’s prank. In each of them all numbers are distinct. Your task is to construct the shortest sequence $\mbox{S}$ that might have been the original $\mbox{M}$. If there are many such sequences, return the lexicographically smallest one. It is guaranteed that such a sequence exists.

Note 

Sequence $A[1\ldots n]$ is lexicographically less than sequence $B[1\ldots n]$ if and only if there exists $1\leq i\leq n$ such that for all $1\leq j\lt i,A[j]=B[j]\:\textit{and}\:\:A[i]\lt B[i]$.

Input Format

In the first line, there is one number $N$ denoting the number of copies of $\mbox{M}$. 

This is followed by $\mbox{K}$ 

and in next line a sequence of length $\mbox{K}$ representing one of sequences after Mary's prank. All numbers are separated by a single space.  

Constraints 

$1\leq N\leq10^3$ 

$2\leq K\leq10^3$ 

All values in one sequence are distinct numbers in range $[1,10^{6}]$.

Output Format

In one line, write the space-separated sequence $\mbox{S}$ - the shortest sequence that might have been the original $\mbox{M}$. If there are many such sequences, return the lexicographically smallest one.

Sample Input
2
2
1 3
3
2 3 4

Sample Output
 1 2 3 4

Explanation

You have 2 copies of the sequence with some missing numbers: $[1,3]$ and $[2,3,4]$. There are two candidates for the original sequence $M:[1,2,3,4]\ \text{and}\ [2,1,3,4]$, where the first one is lexicographically least.
"""

from collections import defaultdict

def reconstruct_sequence(copies):
    before_maps = defaultdict(set)
    after_maps = defaultdict(set)
    
    for sequence in copies:
        prev = 0
        for num in sequence:
            if prev:
                before_maps[num].add(prev)
            after_maps[prev].add(num)
            prev = num
    
    m = []
    actives = set((active for active in after_maps[0] if not before_maps[active]))
    
    while actives:
        next_step = sorted(actives)[0]
        actives.remove(next_step)
        for step in after_maps[next_step]:
            before_maps[step].remove(next_step)
        actives.update((active for active in after_maps[next_step] if not before_maps[active]))
        m.append(next_step)
    
    return m