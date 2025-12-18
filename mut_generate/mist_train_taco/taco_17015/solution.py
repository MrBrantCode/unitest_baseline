"""
QUESTION:
An array is sorted if it has no inversions

A Young Boy

You are given an array of $n$ positive integers $a_1,a_2,\ldots,a_n$.

In one operation you do the following:

Choose any integer $x$.

For all $i$ such that $a_i = x$, do $a_i := 0$ (assign $0$ to $a_i$).

Find the minimum number of operations required to sort the array in non-decreasing order.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). Description of the test cases follows.

The first line of each test case contains a single integer $n$ ($1 \le n \le 10^5$).

The second line of each test case contains $n$ positive integers $a_1,a_2,\ldots,a_n$ ($1 \le a_i \le n$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case print one integer — the minimum number of operations required to sort the array in non-decreasing order.


-----Examples-----

Input
5
3
3 3 2
4
1 3 1 3
5
4 1 5 3 2
4
2 4 1 2
1
1
Output
1
2
4
3
0


-----Note-----

In the first test case, you can choose $x = 3$ for the operation, the resulting array is $[0, 0, 2]$.

In the second test case, you can choose $x = 1$ for the first operation and $x = 3$ for the second operation, the resulting array is $[0, 0, 0, 0]$.
"""

def min_operations_to_sort(test_cases):
    results = []
    for n, array in test_cases:
        data = array[::-1]
        zero_set = set()
        min_value = 10 ** 5 + 1
        end_idx = len(data)
        flag = True
        while flag:
            for (i, num) in enumerate(data[:end_idx]):
                if num in zero_set:
                    min_value = 0
                elif min_value >= num:
                    min_value = num
                else:
                    zero_set = zero_set.union(set(data[i:]))
                    end_idx = i
                    min_value = 10 ** 5 + 1
                    break
            else:
                flag = False
        results.append(len(zero_set))
    return results