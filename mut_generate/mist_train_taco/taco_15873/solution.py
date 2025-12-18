"""
QUESTION:
You are given the following concurrent program. There are N processes and the i-th process has the following pseudocode: 
    
    
    repeat ni times  
        yi := y  
        y := yi + 1  
    end repeat  
    

Here y is a shared variable. Everything else is local for the process. All actions on a given row are atomic, i.e. when the process starts executing a row it is never interrupted. Beyond that all interleavings are possible, i.e. every process that has yet work to do can be granted the rights to execute its next row. In the beginning y = 0. You will be given an integer W and ni, for i = 1, ... , N. Determine if it is possible that after all processes terminate, y = W, and if it is possible output an arbitrary schedule that will produce this final value.

Input

In the first line of the input you will be given two space separated integers N (1 ≤ N ≤ 100) and W ( - 109 ≤ W ≤ 109). In the second line there are N space separated integers ni (1 ≤ ni ≤ 1000).

Output

On the first line of the output write Yes if it is possible that at the end y = W, or No otherwise. If the answer is No then there is no second line, but if the answer is Yes, then on the second line output a space separated list of integers representing some schedule that leads to the desired result. For more information see note.

Examples

Input

1 10
11


Output

No


Input

2 3
4 4


Output

Yes
1 1 2 1 2 2 2 2 2 1 2 1 1 1 1 2


Input

3 6
1 2 3


Output

Yes
1 1 2 2 2 2 3 3 3 3 3 3

Note

For simplicity, assume that there is no repeat statement in the code of the processes, but the code from the loop is written the correct amount of times. The processes are numbered starting from 1. The list of integers represent which process works on its next instruction at a given step. For example, consider the schedule 1 2 2 1 3. First process 1 executes its first instruction, then process 2 executes its first two instructions, after that process 1 executes its second instruction, and finally process 3 executes its first instruction. The list must consists of exactly 2·Σ i = 1...N ni numbers.
"""

def is_possible_final_value(N, W, ni):
    def ng():
        return False, []

    def ok(schedule):
        return True, schedule

    total = sum(ni)

    if W < 1 or total < W:
        return ng()

    if N == 1:
        if W == ni[0]:
            return ok([1] * (ni[0] * 2))
        else:
            return ng()

    if W == 1:
        if min(ni) > 1:
            return ng()
        min_i = ni.index(1) + 1
        ans = []
        for i in range(1, N + 1):
            if i == min_i:
                continue
            ans += [i] * (ni[i - 1] * 2)
        return ok([min_i] + ans + [min_i])

    ans1, ans2, ans3 = [], [], []
    w = W - 2

    if w:
        for i in range(1, 3):
            x = min(ni[i - 1] - 1, w)
            w -= x
            ni[i - 1] -= x
            ans3 += [i] * (2 * x)
        for i in range(3, N + 1):
            x = min(ni[i - 1], w)
            w -= x
            ni[i - 1] -= x
            ans3 += [i] * (2 * x)

    ans1 = [2] * ((ni[1] - 1) * 2)
    for i in range(3, N + 1):
        ans1 += [i] * (ni[i - 1] * 2)
    ans1 = [1] + ans1 + [1]
    ni[0] -= 1
    ans2 = [2] + [1] * (ni[0] * 2) + [2]

    if w == 0:
        return ok(ans1 + ans2 + ans3)
    else:
        return ng()