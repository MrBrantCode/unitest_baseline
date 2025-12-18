"""
QUESTION:
You need to create a function named `fairCandySwap` that takes two lists `A` and `B` as input, representing the sizes of Alice's and Bob's candy bars, respectively. The function should return a list of two integers, where the first integer is the size of the candy bar Alice should swap, and the second integer is the size of the candy bar Bob should swap. The goal is to make the total amount of candy Alice and Bob possess equal after the swap. A solution is guaranteed to exist, and you can return any valid solution if there are multiple. The input lists have the following constraints: 1 <= len(A), len(B) <= 10000 and 1 <= A[i], B[i] <= 100000.
"""

def fair_candy_swap(A, B):
    sumA, sumB = sum(A), sum(B)
    setB = set(B)
    
    for x in A:
        if x + (sumB - sumA)//2 in setB:
            return [x, x + (sumB - sumA)//2]