"""
QUESTION:
Berland scientists noticed long ago that the world around them depends on Berland population. Due to persistent research in this area the scientists managed to find out that the Berland chronology starts from the moment when the first two people came to that land (it is considered to have happened in the first year). After one Berland year after the start of the chronology the population had already equaled 13 people (the second year). However, tracing the population number during the following years was an ultimately difficult task, still it was found out that if di — the number of people in Berland in the year of i, then either di = 12di - 2, or di = 13di - 1 - 12di - 2. Of course no one knows how many people are living in Berland at the moment, but now we can tell if there could possibly be a year in which the country population equaled A. That's what we ask you to determine. Also, if possible, you have to find out in which years it could be (from the beginning of Berland chronology). Let's suppose that it could be in the years of a1, a2, ..., ak. Then you have to define how many residents could be in the country during those years apart from the A variant. Look at the examples for further explanation.

Input

The first line contains integer A (1 ≤ A < 10300). It is guaranteed that the number doesn't contain leading zeros.

Output

On the first output line print YES, if there could be a year in which the total population of the country equaled A, otherwise print NO. 

If the answer is YES, then you also have to print number k — the number of years in which the population could equal A. On the next line you have to output precisely k space-separated numbers — a1, a2, ..., ak. Those numbers have to be output in the increasing order.

On the next line you should output number p — how many variants of the number of people could be in the years of a1, a2, ..., ak, apart from the A variant. On each of the next p lines you have to print one number — the sought number of residents. Those number also have to go in the increasing order. 

If any number (or both of them) k or p exceeds 1000, then you have to print 1000 instead of it and only the first 1000 possible answers in the increasing order.

The numbers should have no leading zeros.

Examples

Input

2


Output

YES
1
1
0


Input

3


Output

NO


Input

13


Output

YES
1
2
0


Input

1729


Output

YES
1
4
1
156
"""

def check_berland_population(A):
    p = []
    c = 1
    for _ in range(600):
        p.append(c)
        c *= 12
    
    r = []
    for i in range(600):
        for j in range(i + 1):
            if p[j] + p[i - j] == A:
                r.append(i + 1)
                break
    
    s = set()
    for i in r:
        for j in range(i):
            v = p[j] + p[i - 1 - j]
            if v != A:
                s.add(v)
    
    can_exist = len(r) > 0
    years = r[:1000] if len(r) > 1000 else r
    other_variants = sorted(s)[:1000] if len(s) > 1000 else sorted(s)
    
    return can_exist, years, other_variants