"""
QUESTION:
Nezzar has a binary string s of length n that he wants to share with his best friend, Nanako. Nanako will spend q days inspecting the binary string. At the same time, Nezzar wants to change the string s into string f during these q days, because it looks better.

It is known that Nanako loves consistency so much. On the i-th day, Nanako will inspect a segment of string s from position l_i to position r_i inclusive. If the segment contains both characters '0' and '1', Nanako becomes unhappy and throws away the string.

After this inspection, at the i-th night, Nezzar can secretly change strictly less than half of the characters in the segment from l_i to r_i inclusive, otherwise the change will be too obvious.

Now Nezzar wonders, if it is possible to avoid Nanako being unhappy and at the same time have the string become equal to the string f at the end of these q days and nights.

Input

The first line contains a single integer t (1 ≤ t ≤ 2 ⋅ 10^5) — the number of test cases.

The first line of each test case contains two integers n,q (1 ≤ n ≤ 2 ⋅ 10^5, 0 ≤ q ≤ 2 ⋅ 10^5).

The second line of each test case contains a binary string s of length n.

The third line of each test case contains a binary string f of length n.

Then q lines follow, i-th of them contains two integers l_i,r_i (1 ≤ l_i ≤ r_i ≤ n) — bounds of the segment, that Nanako will inspect on the i-th day.

It is guaranteed that the sum of n for all test cases doesn't exceed 2 ⋅ 10^5, and the sum of q for all test cases doesn't exceed 2 ⋅ 10^5.

Output

For each test case, print "YES" on the single line if it is possible to avoid Nanako being unhappy and have the string f at the end of q days and nights. Otherwise, print "NO".

You can print each letter in any case (upper or lower).

Example

Input


4
5 2
00000
00111
1 5
1 3
2 1
00
01
1 2
10 6
1111111111
0110001110
1 10
5 9
7 10
1 7
3 5
6 10
5 2
10000
11000
2 5
1 3


Output


YES
NO
YES
NO

Note

In the first test case, \underline{00000} → \underline{000}11 → 00111 is one of the possible sequences of string changes.

In the second test case, it can be shown that it is impossible to have the string f at the end.
"""

def can_transform_string(n, q, s, f, inspections):
    sn = 1 << n.bit_length()
    node = [0] * sn + [int(c) for c in f] + [0] * (sn - n)
    label = [-1] * (2 * sn)
    
    for i in range(sn - 1, 0, -1):
        node[i] = node[i << 1] + node[i << 1 | 1]
    
    def set_range(lx, rx, v, now):
        if l <= lx and r >= rx:
            label[now] = v
            node[now] = (rx - lx) if v else 0
            return
        mx = lx + rx >> 1
        nl = now << 1
        nr = nl + 1
        if label[now] != -1:
            node[nl] = node[nr] = node[now] >> 1
            label[nl] = label[nr] = label[now]
            label[now] = -1
        if l < mx:
            set_range(lx, mx, v, nl)
        if r > mx:
            set_range(mx, rx, v, nr)
        node[now] = node[nl] + node[nr]
    
    def get_range(lx, rx, now):
        if l <= lx and r >= rx:
            return node[now]
        mx = lx + rx >> 1
        nl = now << 1
        nr = nl + 1
        if label[now] != -1:
            return min(rx, r) - max(lx, l) if label[now] else 0
        m1 = get_range(lx, mx, nl) if l < mx else 0
        m2 = get_range(mx, rx, nr) if r > mx else 0
        return m1 + m2
    
    def match(lx, rx, now):
        if lx >= n:
            return False
        if now >= sn:
            return node[now] != int(s[lx])
        if label[now] != -1:
            return any((v != label[now] for v in s[lx:rx]))
        mx = rx + lx >> 1
        return match(lx, mx, now << 1) or match(mx, rx, now << 1 | 1)
    
    f = True
    for (l, r) in inspections[::-1]:
        l -= 1
        count = get_range(0, sn, 1) * 2
        if count == r - l:
            f = False
            break
        set_range(0, sn, 1 if count > r - l else 0, 1)
    
    return f and (not match(0, sn, 1))