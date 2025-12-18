"""
QUESTION:
The only difference between the two versions is that in this version $n \leq 1000$ and the sum of $n$ over all test cases does not exceed $1000$.

A terminal is a row of $n$ equal segments numbered $1$ to $n$ in order. There are two terminals, one above the other.

You are given an array $a$ of length $n$. For all $i = 1, 2, \dots, n$, there should be a straight wire from some point on segment $i$ of the top terminal to some point on segment $a_i$ of the bottom terminal. You can't select the endpoints of a segment. For example, the following pictures show two possible wirings if $n=7$ and $a=[4,1,4,6,7,7,5]$.

A crossing occurs when two wires share a point in common. In the picture above, crossings are circled in red.

What is the maximum number of crossings there can be if you place the wires optimally?


-----Input-----

The first line contains an integer $t$ ($1 \leq t \leq 1000$) — the number of test cases.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 1000$) — the length of the array.

The second line of each test case contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \leq a_i \leq n$) — the elements of the array.

The sum of $n$ across all test cases does not exceed $1000$.


-----Output-----

For each test case, output a single integer — the maximum number of crossings there can be if you place the wires optimally.


-----Examples-----

Input
4
7
4 1 4 6 7 7 5
2
2 1
1
1
3
2 2 2
Output
6
1
0
3


-----Note-----

The first test case is shown in the second picture in the statement.

In the second test case, the only wiring possible has the two wires cross, so the answer is $1$.

In the third test case, the only wiring possible has one wire, so the answer is $0$.
"""

from collections import defaultdict

def calculate_max_crossings(test_cases):
    def reversePairs(nums):
        ans = 0

        def getReverse(lst):
            nonlocal ans
            if len(lst) < 2:
                return lst
            half = len(lst) // 2
            half_ = len(lst) - len(lst) // 2
            (first_half, second_half) = (getReverse(lst[:half]), getReverse(lst[half:]))
            lst = []
            i1 = 0
            i2 = 0
            while i1 < half or i2 < half_:
                if i1 == half:
                    lst += second_half[i2:]
                    break
                if i2 == half_:
                    lst += first_half[i1:]
                    ans += (half - i1) * i2
                    break
                if first_half[i1] <= second_half[i2]:
                    lst.append(first_half[i1])
                    i1 += 1
                    ans += i2
                else:
                    lst.append(second_half[i2])
                    i2 += 1
            return lst
        getReverse(nums)
        return ans

    results = []
    for n, a in test_cases:
        tmp_lst = []
        d = defaultdict(int)
        for num in a:
            d[num] -= 1
            tmp_lst.append((num, d[num]))
        results.append(reversePairs(tmp_lst))
    
    return results