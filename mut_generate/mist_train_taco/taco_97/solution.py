"""
QUESTION:
You are situated in an N dimensional grid at position (x1,x2,...,xN). The dimensions of the grid are (D1,D2,...DN). In one step, you can walk one step ahead or behind in any one of the N dimensions. (So there are always 2×N possible different moves). In how many ways can you take M steps such that you do not leave the grid at any point? You leave the grid if at any point xi, either xi≤0 or xi>Di. 

Input Format

The first line contains the number of test cases T. T test cases follow. For each test case, the first line contains N and M, the second line contains x1,x2,…,xN and the 3rd line contains D1,D2,…,DN.

Output Format

Output T lines, one corresponding to each test case. Since the answer can be really huge, output it modulo 1000000007.

Constraints

1≤T≤10

1≤N≤10

1≤M≤300

1≤Di≤100

1≤xi≤Di

SAMPLE INPUT
5
1 287
44
78
1 236
25
87
1 122
41
63
1 260
7
64
1 127
3
73

SAMPLE OUTPUT
38753340
587915072
644474045
423479916
320130104
"""

def calculate_ways(n, m, starting_point, dimensions):
    def ways(di, offset, steps):
        if steps in mem[di] and offset in mem[di][steps]:
            return mem[di][steps][offset]
        val = 0
        if steps == 0:
            val = 1
        else:
            if offset - 1 >= 1:
                val += ways(di, offset - 1, steps - 1)
            if offset + 1 <= dimensions[di]:
                val += ways(di, offset + 1, steps - 1)
        mem[di][steps][offset] = val
        return val

    def set_ways(left, right, steps):
        if (left, right) in mem_set and steps in mem_set[(left, right)]:
            return mem_set[(left, right)][steps]
        if right - left == 1:
            return mem[left][steps][starting_point[left]]
        val = 0
        split_point = left + (right - left) // 2
        for i in range(steps + 1):
            t1 = i
            t2 = steps - i
            mix_factor = fact[steps] // (fact[t1] * fact[t2])
            val += mix_factor * set_ways(left, split_point, t1) * set_ways(split_point, right, t2)
        mem_set[(left, right)][steps] = val
        return val

    fact = {0: 1}
    accum = 1
    for k in range(1, 300 + 1):
        accum *= k
        fact[k] = accum

    mem = {}
    for di in range(n):
        mem[di] = {}
        for i in range(m + 1):
            mem[di][i] = {}
            ways(di, starting_point[di], i)

    mem_set = {}
    for i in range(n + 1):
        for j in range(n + 1):
            mem_set[(i, j)] = {}

    answer = set_ways(0, n, m)
    return answer % 1000000007