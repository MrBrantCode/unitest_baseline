"""
QUESTION:
Ivan has an array consisting of n elements. Each of the elements is an integer from 1 to n.

Recently Ivan learned about permutations and their lexicographical order. Now he wants to change (replace) minimum number of elements in his array in such a way that his array becomes a permutation (i.e. each of the integers from 1 to n was encountered in his array exactly once). If there are multiple ways to do it he wants to find the lexicographically minimal permutation among them.

Thus minimizing the number of changes has the first priority, lexicographical minimizing has the second priority.

In order to determine which of the two permutations is lexicographically smaller, we compare their first elements. If they are equal — compare the second, and so on. If we have two permutations x and y, then x is lexicographically smaller if x_{i} < y_{i}, where i is the first index in which the permutations x and y differ.

Determine the array Ivan will obtain after performing all the changes.


-----Input-----

The first line contains an single integer n (2 ≤ n ≤ 200 000) — the number of elements in Ivan's array.

The second line contains a sequence of integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ n) — the description of Ivan's array.


-----Output-----

In the first line print q — the minimum number of elements that need to be changed in Ivan's array in order to make his array a permutation. In the second line, print the lexicographically minimal permutation which can be obtained from array with q changes.


-----Examples-----
Input
4
3 2 2 3

Output
2
1 2 4 3 

Input
6
4 5 6 3 2 1

Output
0
4 5 6 3 2 1 

Input
10
6 8 4 6 7 1 6 3 4 5

Output
3
2 8 4 6 7 1 9 3 10 5 



-----Note-----

In the first example Ivan needs to replace number three in position 1 with number one, and number two in position 3 with number four. Then he will get a permutation [1, 2, 4, 3] with only two changed numbers — this permutation is lexicographically minimal among all suitable. 

In the second example Ivan does not need to change anything because his array already is a permutation.
"""

def minimal_permutation(n, a):
    # Convert array elements to zero-based indexing
    for i in range(n):
        a[i] = a[i] - 1
    
    # Dictionary to count occurrences of each element
    occ = {}
    for i in range(n):
        if a[i] not in occ:
            occ[a[i]] = 1
        else:
            occ[a[i]] += 1
    
    # List to store missing elements
    missing = []
    for i in range(n):
        if i not in occ:
            missing.append(i)
    
    # Index for the missing elements list
    act_missing = 0
    
    # List to keep track of remaining occurrences of each element
    left = [1] * n
    
    # Iterate through the array to make changes
    for pos in range(n):
        if a[pos] in occ and occ[a[pos]] > left[a[pos]]:
            if act_missing < len(missing) and (missing[act_missing] < a[pos] or left[a[pos]] == 0):
                occ[a[pos]] -= 1
                a[pos] = missing[act_missing]
                act_missing += 1
            else:
                left[a[pos]] -= 1
                occ[a[pos]] -= 1
    
    # Convert array elements back to one-based indexing
    for i in range(n):
        a[i] = a[i] + 1
    
    # Return the number of changes and the resulting permutation
    return len(missing), a