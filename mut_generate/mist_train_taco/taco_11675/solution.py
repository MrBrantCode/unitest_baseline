"""
QUESTION:
Little Artem has invented a time machine! He could go anywhere in time, but all his thoughts of course are with computer science. He wants to apply this time machine to a well-known data structure: multiset.

Artem wants to create a basic multiset of integers. He wants these structure to support operations of three types:

  1. Add integer to the multiset. Note that the difference between set and multiset is that multiset may store several instances of one integer. 
  2. Remove integer from the multiset. Only one instance of this integer is removed. Artem doesn't want to handle any exceptions, so he assumes that every time remove operation is called, that integer is presented in the multiset. 
  3. Count the number of instances of the given integer that are stored in the multiset. 



But what about time machine? Artem doesn't simply apply operations to the multiset one by one, he now travels to different moments of time and apply his operation there. Consider the following example.

  * First Artem adds integer 5 to the multiset at the 1-st moment of time. 
  * Then Artem adds integer 3 to the multiset at the moment 5. 
  * Then Artem asks how many 5 are there in the multiset at moment 6. The answer is 1. 
  * Then Artem returns back in time and asks how many integers 3 are there in the set at moment 4. Since 3 was added only at moment 5, the number of integers 3 at moment 4 equals to 0. 
  * Then Artem goes back in time again and removes 5 from the multiset at moment 3. 
  * Finally Artyom asks at moment 7 how many integers 5 are there in the set. The result is 0, since we have removed 5 at the moment 3. 



Note that Artem dislikes exceptions so much that he assures that after each change he makes all delete operations are applied only to element that is present in the multiset. The answer to the query of the third type is computed at the moment Artem makes the corresponding query and are not affected in any way by future changes he makes.

Help Artem implement time travellers multiset.

Input

The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of Artem's queries.

Then follow n lines with queries descriptions. Each of them contains three integers ai, ti and xi (1 ≤ ai ≤ 3, 1 ≤ ti, xi ≤ 109) — type of the query, moment of time Artem travels to in order to execute this query and the value of the query itself, respectively. It's guaranteed that all moments of time are distinct and that after each operation is applied all operations of the first and second types are consistent.

Output

For each ask operation output the number of instances of integer being queried at the given moment of time.

Examples

Input

6
1 1 5
3 5 5
1 2 5
3 6 5
2 3 5
3 7 5


Output

1
2
1


Input

3
1 1 1
2 2 1
3 3 1


Output

0
"""

def time_traveller_multiset(n, queries):
    from collections import defaultdict

    def compress_coordinate(lst):
        return {i: ind + 1 for (ind, i) in enumerate(sorted(set(lst)))}

    def build_bit(bit, n):
        for i in range(1, n + 1):
            x = new(i)
            if x <= n:
                bit[x] += bit[i]

    def point_update(bit, point, n, diff):
        while point <= n:
            bit[point] += diff
            point = new(point)

    def calculate_prefix(bit, point):
        su = 0
        while point:
            su += bit[point]
            point &= point - 1
        return su

    def range_query(bit, start, stop):
        return calculate_prefix(bit, stop) - calculate_prefix(bit, start - 1)

    new = lambda xx: (xx | xx - 1) + 1

    dct = defaultdict(list)
    for (a, t, x) in queries:
        dct[x].append(t)

    new_map = {i: compress_coordinate(dct[i]) for i in dct}

    for i in range(n):
        queries[i] = (queries[i][0], new_map[queries[i][2]][queries[i][1]], queries[i][2])

    bit = {i: [0] * (len(dct[i]) + 1) for i in dct}

    results = []
    for (a, t, x) in queries:
        if a == 1:
            point_update(bit[x], t, len(bit[x]) - 1, 1)
        elif a == 2:
            point_update(bit[x], t, len(bit[x]) - 1, -1)
        elif a == 3:
            results.append(calculate_prefix(bit[x], t))

    return results