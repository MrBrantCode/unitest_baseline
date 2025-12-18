"""
QUESTION:
There are N positive integers A_1, A_2, ..., A_N. Takahashi can perform the following operation on these integers any number of times:

* Choose 1 \leq i \leq N and multiply the value of A_i by -2.



Notice that he multiplies it by minus two.

He would like to make A_1 \leq A_2 \leq ... \leq A_N holds. Find the minimum number of operations required. If it is impossible, print `-1`.

Constraints

* 1 \leq N \leq 200000
* 1 \leq A_i \leq 10^9

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the answer.

Examples

Input

4
3 1 4 1


Output

3


Input

5
1 2 3 4 5


Output

0


Input

8
657312726 129662684 181537270 324043958 468214806 916875077 825989291 319670097


Output

7
"""

def min_operations_to_sorted(A):
    def d4(x, y):
        ret = 0
        while x > y:
            y *= 4
            ret += 1
        return ret

    def cost(ls):
        l = len(ls)
        ret = [0] * l
        stack = [(l - 1, 10 ** 18)]
        for i in range(l - 1)[::-1]:
            ret[i] = ret[i + 1]
            if ls[i] <= ls[i + 1]:
                d = d4(ls[i + 1], ls[i]) - 1
                if d > 0:
                    stack.append((i, d))
            else:
                d = d4(ls[i], ls[i + 1])
                while d:
                    (idx, num) = stack.pop()
                    if d > num:
                        ret[i] += (idx - i) * num
                        d -= num
                    else:
                        ret[i] += (idx - i) * d
                        num -= d
                        d = 0
                        if num:
                            stack.append((idx, num))
        return ret

    cp = cost(A)
    cn = cost(A[::-1])
    n = len(A)
    
    for i in range(n):
        cp[i] *= 2
        cn[i] *= 2
        cn[i] += n - i
    
    ansls = [cp[0], cn[0]]
    for i in range(1, n):
        ansls.append(cp[i] + cn[n - i])
    
    return min(ansls)