"""
QUESTION:
There is a sale in the market on clothes , so as usual N girls gathered there to grab great deals.But due to huge popularity of sale crowd has gone uncontrollable. You being head of management team of the mall has been assigned the task to make them form a queue so that everyone can shop turn-wise.
Since queue is going to be very long and knowing that its gonna take time for their turn there are M pair of girls who want to stand together in the queue so that they can discuss their personal stuff meanwhile.
Now you need to make them form a  queue so that none of them gets disappointed.

INPUT:

First line of input contains T number of test-cases , first line of each test-case contains two elements N , M total number of girls and number of pair of girls who wants to stand together.
Next M line will contain pair of integers x y , which mean in queue they either stand as x y or y x .

OUTPUT:

For each test-case in a new line output "NO" ( without quotes ) if there is no possible arrangement such that no one gets disappointed if such a arrangement is possible print "YES" ( without quotes ) .

Constraints:

1 ≤ T ≤ 10

N  , M ≤ 10 ^ 5 

SAMPLE INPUT
2
5 3
1 2
3 4
2 5
4 3
1 2
1 3
1 4

SAMPLE OUTPUT
YES
NO
"""

def can_form_queue(n, m, pairs):
    from collections import defaultdict
    
    def solve(v, a, visit, parent):
        visit[v] = 1
        for i in a[v]:
            if visit[i] == 0:
                if solve(i, a, visit, v):
                    return True
            elif i != parent:
                return True
        return False
    
    visit = [0] * (n + 1)
    a = defaultdict(list)
    
    for x, y in pairs:
        a[x].append(y)
        a[y].append(x)
    
    check = 0
    for x in range(1, n + 1):
        if visit[x] == 0:
            check = solve(x, a, visit, -1)
        if len(a[x]) > 2:
            check = 1
        if check == 1:
            break
    
    return "NO" if check == 1 else "YES"