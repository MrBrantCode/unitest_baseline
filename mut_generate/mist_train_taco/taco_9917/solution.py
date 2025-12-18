"""
QUESTION:
Vasya has an array a consisting of positive integer numbers. Vasya wants to divide this array into two non-empty consecutive parts (the prefix and the suffix) so that the sum of all elements in the first part equals to the sum of elements in the second part. It is not always possible, so Vasya will move some element before dividing the array (Vasya will erase some element and insert it into an arbitrary position).

Inserting an element in the same position he was erased from is also considered moving.

Can Vasya divide the array after choosing the right element to move and its new position?


-----Input-----

The first line contains single integer n (1 ≤ n ≤ 100000) — the size of the array.

The second line contains n integers a_1, a_2... a_{n} (1 ≤ a_{i} ≤ 10^9) — the elements of the array.


-----Output-----

Print YES if Vasya can divide the array after moving one element. Otherwise print NO.


-----Examples-----
Input
3
1 3 2

Output
YES

Input
5
1 2 3 4 5

Output
NO

Input
5
2 2 3 4 5

Output
YES



-----Note-----

In the first example Vasya can move the second element to the end of the array.

In the second example no move can make the division possible.

In the third example Vasya can move the fourth element by one position to the left.
"""

def can_divide_array_after_move(n, a):
    from collections import Counter
    
    s = sum(a)
    c1 = Counter(a)
    c2 = Counter()
    cur = 0
    
    for x in a:
        c1[x] -= 1
        c2[x] += 1
        cur += x
        s1 = cur
        s2 = s - s1
        
        if s1 == s2:
            return 'YES'
        
        if (s2 - s1) % 2 == 1:
            continue
        
        if s2 > s1:
            if c1[(s2 - s1) // 2] > 0:
                return 'YES'
        elif c2[(s1 - s2) // 2] > 0:
            return 'YES'
    
    return 'NO'