"""
QUESTION:
Let's arrange a deck of cards. Your task is to sort totally n cards. A card consists of a part of a suit (S, H, C or D) and an number. Write a program which sorts such cards based on the following pseudocode:


Partition(A, p, r)
1 x = A[r]
2 i = p-1
3 for j = p to r-1
4     do if A[j] <= x
5        then i = i+1
6            exchange A[i] and A[j]
7 exchange A[i+1] and A[r]
8 return i+1


Quicksort(A, p, r)
1 if p < r
2    then q = Partition(A, p, r)
3        run Quicksort(A, p, q-1)
4        run Quicksort(A, q+1, r)


Here, A is an array which represents a deck of cards and comparison operations are performed based on the numbers.

Your program should also report the stability of the output for the given input (instance). Here, 'stability of the output' means that: cards with the same value appear in the output in the same order as they do in the input (instance).

Constraints

* 1 ≤ n ≤ 100,000
* 1 ≤ the number of a card ≤ 109
* There are no identical card in the input

Input

The first line contains an integer n, the number of cards.

n cards are given in the following lines. Each card is given in a line and represented by a pair of a character and an integer separated by a single space.

Output

In the first line, print the stability ("Stable" or "Not stable") of this output.

In the following lines, print the arranged cards in the same manner of that of the input.

Examples

Input

6
D 3
H 2
D 1
S 3
D 2
C 1


Output

Not stable
D 1
C 1
D 2
H 2
D 3
S 3


Input

2
S 1
H 1


Output

Stable
S 1
H 1
"""

def sort_and_check_stability(cards, n):
    def partition(A, p, r):
        x = A[r][1]
        i = p - 1
        for j in range(p, r):
            if A[j][1] <= x:
                i += 1
                (A[i], A[j]) = (A[j], A[i])
        (A[i + 1], A[r]) = (A[r], A[i + 1])
        return i + 1

    def quick_sort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quick_sort(A, p, q - 1)
            quick_sort(A, q + 1, r)

    # Create a dictionary to store the original indices of the cards
    ind = dict(((e, i) for (i, e) in enumerate(cards)))
    
    # Perform the quick sort
    quick_sort(cards, 0, n - 1)
    
    # Check for stability
    for i in range(n - 1):
        if cards[i][1] == cards[i + 1][1]:
            if ind[cards[i]] > ind[cards[i + 1]]:
                return 'Not stable', cards
    return 'Stable', cards