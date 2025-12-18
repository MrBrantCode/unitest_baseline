"""
QUESTION:
You are given a permutation of integers from 1 to n. Exactly once you apply the following operation to this permutation: pick a random segment and shuffle its elements. Formally:  Pick a random segment (continuous subsequence) from l to r. All $\frac{n(n + 1)}{2}$ segments are equiprobable.  Let k = r - l + 1, i.e. the length of the chosen segment. Pick a random permutation of integers from 1 to k, p_1, p_2, ..., p_{k}. All k! permutation are equiprobable.  This permutation is applied to elements of the chosen segment, i.e. permutation a_1, a_2, ..., a_{l} - 1, a_{l}, a_{l} + 1, ..., a_{r} - 1, a_{r}, a_{r} + 1, ..., a_{n} is transformed to a_1, a_2, ..., a_{l} - 1, a_{l} - 1 + p_1, a_{l} - 1 + p_2, ..., a_{l} - 1 + p_{k} - 1, a_{l} - 1 + p_{k}, a_{r} + 1, ..., a_{n}. 

Inversion if a pair of elements (not necessary neighbouring) with the wrong relative order. In other words, the number of inversion is equal to the number of pairs (i, j) such that i < j and a_{i} > a_{j}. Find the expected number of inversions after we apply exactly one operation mentioned above.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 100 000) — the length of the permutation.

The second line contains n distinct integers from 1 to n — elements of the permutation.


-----Output-----

Print one real value — the expected number of inversions. Your answer will be considered correct if its absolute or relative error does not exceed 10^{ - 9}. 

Namely: let's assume that your answer is a, and the answer of the jury is b. The checker program will consider your answer correct, if $\frac{|a - b|}{\operatorname{max}(1, b)} \leq 10^{-9}$.


-----Example-----
Input
3
2 3 1

Output
1.916666666666666666666666666667
"""

def calculate_expected_inversions(n, permutation):
    def getSum(BITree, index):
        sum = 0
        while index > 0:
            sum += BITree[index]
            index -= index & -index
        return sum

    def updateBIT(BITree, n, index, val):
        while index <= n:
            BITree[index] += val
            index += index & -index

    def getInvCount(arr, n):
        invcount = 0
        maxElement = max(arr)
        BIT = [0] * (maxElement + 1)
        for i in range(1, maxElement + 1):
            BIT[i] = 0
        for i in range(n - 1, -1, -1):
            invcount += getSum(BIT, arr[i] - 1)
            updateBIT(BIT, maxElement, arr[i], 1)
        return invcount

    def getInvCountAdv(arr, n):
        invcount = 0
        maxElement = max(arr)
        BIT = [0] * (maxElement + 1)
        for i in range(1, maxElement + 1):
            BIT[i] = 0
        for i in range(n - 1, -1, -1):
            invcount += (i + 1) * getSum(BIT, arr[i] - 1)
            updateBIT(BIT, maxElement, arr[i], n - i)
        return invcount

    InvCount = getInvCount(permutation, n)
    InvCountAdv = getInvCountAdv(permutation, n)
    thirdSum = 0
    for i in range(1, n + 1):
        thirdSum += i * (i - 1) * (n - i + 1) / 2

    expected_inversions = InvCount - InvCountAdv / (n * (n + 1)) * 2 + thirdSum / (n * (n + 1))
    return expected_inversions