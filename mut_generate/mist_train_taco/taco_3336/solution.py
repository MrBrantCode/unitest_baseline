"""
QUESTION:
problem

Given the sequence $ A $ of length $ N $. The $ i $ item in $ A $ is $ A_i $. You can do the following for this sequence:

* $ 1 \ leq i \ leq N --Choose the integer i that is 1 $. Swap the value of $ A_i $ with the value of $ A_ {i + 1} $.



Find the minimum number of operations required to make $ A $ a sequence of bumps.

A sequence of length $ N $ that satisfies the following conditions is defined as a sequence of irregularities.

* For any $ i $ that satisfies $ 1 <i <N $, ​​$ A_ {i + 1}, A_ {i --1}> A_i $ or $ A_ {i + 1}, A_ {i --1} <A_i Satisfy $.
Intuitively, increase, decrease, increase ... (decrease, like $ 1, \ 10, \ 2, \ 30, \ \ dots (10, \ 1, \ 30, \ 2, \ \ dots) $ It is a sequence that repeats increase, decrease ...).



output

Output the minimum number of operations required to make a sequence of bumps. Also, output a line break at the end.

Example

Input

5
1 2 3 4 5


Output

2
"""

def min_operations_to_bump_sequence(A):
    n = len(A)
    if n < 2:
        return 0
    
    def count_operations(start_with_increase):
        b = A[:]
        s = 0
        for i in range(1, n):
            if (i % 2 == 1) == start_with_increase:
                if b[i] > b[i - 1]:
                    flag = True
                    if i < n - 1:
                        if b[i - 1] > b[i + 1] and b[i + 1] < b[i]:
                            b[i], b[i + 1] = b[i + 1], b[i]
                            flag = False
                    if flag:
                        b[i], b[i - 1] = b[i - 1], b[i]
                    s += 1
            else:
                if b[i] < b[i - 1]:
                    flag = True
                    if i < n - 1:
                        if b[i - 1] < b[i + 1] and b[i + 1] > b[i]:
                            b[i], b[i + 1] = b[i + 1], b[i]
                            flag = False
                    if flag:
                        b[i], b[i - 1] = b[i - 1], b[i]
                    s += 1
        return s
    
    ans = min(count_operations(True), count_operations(False))
    return ans