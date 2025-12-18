"""
QUESTION:
Everybody knows what an arithmetic progression is. 

Sequences [1, 5], [10], [5, 4, 3] are arithmetic progressions and sequences [1, 3, 2], [1, 2, 4] are not.

Alexander has n cards containing integers. Arthur wants to give Alexander exactly one more card with a number so that he could use the resulting n+1 cards to make an arithmetic progression (Alexander has to use all of his cards).

Arthur has already bought a card but he hasn't written a number on it. Help him, print all integers that you can write on a card so that the described condition fulfilled.

Input

The first line contains integer n (1 ≤ n ≤ 10^5) — the number of cards. The next line contains the sequence of integers — the numbers on Alexander's cards. The numbers are positive integers, each of them doesn't exceed 10^8.

Output

If Arthur can write infinitely many distinct integers on the card, print on a single line -1.

Otherwise, print on the first line the number of integers that suit you. In the second line, print the numbers in the increasing order. Note that the numbers in the answer can exceed 10^8 or even be negative.

SAMPLE INPUT
3
4 1 7

SAMPLE OUTPUT
2
-2 10

Explanation

Adding both of these numbers makes the sorted sequence in AP.
"""

def find_arithmetic_progression_numbers(n, arr):
    if n <= 1:
        return (-1, [])
    
    arr.sort()
    
    if n == 2:
        diff = arr[1] - arr[0]
        if diff % 2 == 0:
            return (3, [2 * arr[0] - arr[1], (arr[0] + arr[1]) // 2, 2 * arr[1] - arr[0]])
        else:
            return (2, [2 * arr[0] - arr[1], 2 * arr[1] - arr[0]])
    
    di = arr[1] - arr[0]
    i = 1
    while i + 1 < n and arr[i + 1] - arr[i] == di:
        i += 1
    
    dj = arr[n - 1] - arr[n - 2]
    j = n - 2
    while j - 1 >= 0 and arr[j] - arr[j - 1] == dj:
        j -= 1
    
    if j < i:
        if di == dj == 0:
            return (1, [arr[0]])
        else:
            return (2, [arr[0] - di, arr[n - 1] + di])
    elif j == i:
        if i == 1 and di == 2 * dj:
            return (1, [arr[0] + dj])
        elif j == n - 2 and dj == 2 * di:
            return (1, [arr[n - 1] - di])
        else:
            return (0, [])
    elif j == i + 1:
        if di == dj and arr[i] + di == arr[j] - dj:
            return (1, [arr[i] + di])
        else:
            return (0, [])
    else:
        return (0, [])