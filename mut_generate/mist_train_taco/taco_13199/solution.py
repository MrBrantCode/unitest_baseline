"""
QUESTION:
Greg has an array a = a1, a2, ..., an and m operations. Each operation looks as: li, ri, di, (1 ≤ li ≤ ri ≤ n). To apply operation i to the array means to increase all array elements with numbers li, li + 1, ..., ri by value di.

Greg wrote down k queries on a piece of paper. Each query has the following form: xi, yi, (1 ≤ xi ≤ yi ≤ m). That means that one should apply operations with numbers xi, xi + 1, ..., yi to the array.

Now Greg is wondering, what the array a will be after all the queries are executed. Help Greg.

Input

The first line contains integers n, m, k (1 ≤ n, m, k ≤ 105). The second line contains n integers: a1, a2, ..., an (0 ≤ ai ≤ 105) — the initial array.

Next m lines contain operations, the operation number i is written as three integers: li, ri, di, (1 ≤ li ≤ ri ≤ n), (0 ≤ di ≤ 105).

Next k lines contain the queries, the query number i is written as two integers: xi, yi, (1 ≤ xi ≤ yi ≤ m).

The numbers in the lines are separated by single spaces.

Output

On a single line print n integers a1, a2, ..., an — the array after executing all the queries. Separate the printed numbers by spaces.

Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams of the %I64d specifier.

Examples

Input

3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2
1 3
2 3


Output

9 18 17


Input

1 1 1
1
1 1 1
1 1


Output

2


Input

4 3 6
1 2 3 4
1 2 1
2 3 2
3 4 4
1 2
1 3
2 3
1 2
1 3
2 3


Output

5 18 31 20
"""

def apply_operations_and_queries(n, m, k, a, operations, queries):
    temp = [0] * (n + 1)
    queries_count = [0] * (m + 1)
    
    # Process queries to count how many times each operation should be applied
    for x, y in queries:
        queries_count[x - 1] += 1
        if y < m:
            queries_count[y] -= 1
    
    # Apply operations based on the query counts
    num_queries = 0
    for i in range(m):
        num_queries += queries_count[i]
        li, ri, di = operations[i]
        temp[li - 1] += num_queries * di
        if ri < n:
            temp[ri] -= num_queries * di
    
    # Apply the accumulated changes to the array a
    x = temp[0]
    result = [x + a[0]]
    for i in range(1, n):
        x += temp[i]
        result.append(x + a[i])
    
    return result