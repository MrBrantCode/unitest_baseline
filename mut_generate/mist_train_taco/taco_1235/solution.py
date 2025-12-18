"""
QUESTION:
An infinitely long railway has a train consisting of n cars, numbered from 1 to n (the numbers of all the cars are distinct) and positioned in arbitrary order. David Blaine wants to sort the railway cars in the order of increasing numbers. In one move he can make one of the cars disappear from its place and teleport it either to the beginning of the train, or to the end of the train, at his desire. What is the minimum number of actions David Blaine needs to perform in order to sort the train?

Input

The first line of the input contains integer n (1 ≤ n ≤ 100 000) — the number of cars in the train. 

The second line contains n integers pi (1 ≤ pi ≤ n, pi ≠ pj if i ≠ j) — the sequence of the numbers of the cars in the train.

Output

Print a single integer — the minimum number of actions needed to sort the railway cars.

Examples

Input

5
4 1 2 5 3


Output

2


Input

4
4 1 3 2


Output

2

Note

In the first sample you need first to teleport the 4-th car, and then the 5-th car to the end of the train.
"""

def min_actions_to_sort_train(n, L):
    """
    Calculate the minimum number of actions needed to sort the railway cars.

    Parameters:
    n (int): The number of cars in the train.
    L (list of int): The sequence of the numbers of the cars in the train.

    Returns:
    int: The minimum number of actions needed to sort the railway cars.
    """
    def LIS(s):
        n = len(s)
        L = [0] * n
        appear = [False] * n
        L[0] = 1
        find = [-1] * n
        appear[s[0]] = True
        find[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] > 0 and appear[s[i] - 1]:
                L[i] = L[find[s[i] - 1]] + 1
            else:
                L[i] = 1
            appear[s[i]] = True
            find[s[i]] = i
        return max(L)

    def BIS(s):
        n = len(s)
        L = [0] * n
        appear = [False] * n
        L[n - 1] = 1
        find = [-1] * n
        appear[s[n - 1]] = True
        find[s[n - 1]] = n - 1
        for i in range(n - 2, -1, -1):
            if s[i] + 1 < n and appear[s[i] + 1]:
                L[i] = L[find[s[i] - 1]] + 1
            else:
                L[i] = 1
            appear[s[i]] = True
            find[s[i]] = i
        return max(L)

    L = [x - 1 for x in L]
    return n - max(LIS(L), BIS(L))