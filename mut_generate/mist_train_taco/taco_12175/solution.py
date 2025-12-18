"""
QUESTION:
Vasya has a multiset s consisting of n integer numbers. Vasya calls some number x nice if it appears in the multiset exactly once. For example, multiset \{1, 1, 2, 3, 3, 3, 4\} contains nice numbers 2 and 4.

Vasya wants to split multiset s into two multisets a and b (one of which may be empty) in such a way that the quantity of nice numbers in multiset a would be the same as the quantity of nice numbers in multiset b (the quantity of numbers to appear exactly once in multiset a and the quantity of numbers to appear exactly once in multiset b).

Input

The first line contains a single integer n~(2 ≤ n ≤ 100).

The second line contains n integers s_1, s_2, ... s_n~(1 ≤ s_i ≤ 100) — the multiset s.

Output

If there exists no split of s to satisfy the given requirements, then print "NO" in the first line.

Otherwise print "YES" in the first line.

The second line should contain a string, consisting of n characters. i-th character should be equal to 'A' if the i-th element of multiset s goes to multiset a and 'B' if if the i-th element of multiset s goes to multiset b. Elements are numbered from 1 to n in the order they are given in the input.

If there exist multiple solutions, then print any of them.

Examples

Input

4
3 5 7 1


Output

YES
BABA


Input

3
3 5 1


Output

NO
"""

def split_multiset(n, s):
    d = {}
    mt = False
    mti = -1
    
    # Count occurrences of each number in the multiset
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
            if d[s[i]] > 2:
                mt = True
                mti = i
    
    # Identify nice numbers
    good = []
    for key in d.keys():
        if d[key] == 1:
            good.append(key)
    
    # Check if the number of nice numbers is even
    if len(good) % 2 == 0:
        result = 'YES'
        good1 = good[:len(good) // 2]
        assignment = ''.join('A' if i in good1 else 'B' for i in s)
    elif mt:
        result = 'YES'
        good1 = good[:len(good) // 2]
        u = False
        assignment = ''.join('A' if i in good1 or (not u and i == s[mti]) else 'B' for i in s)
    else:
        result = 'NO'
        assignment = ''
    
    return result, assignment