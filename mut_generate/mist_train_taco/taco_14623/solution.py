"""
QUESTION:
In one of the games Arkady is fond of the game process happens on a rectangular field. In the game process Arkady can buy extensions for his field, each extension enlarges one of the field sizes in a particular number of times. Formally, there are n extensions, the i-th of them multiplies the width or the length (by Arkady's choice) by a_{i}. Each extension can't be used more than once, the extensions can be used in any order.

Now Arkady's field has size h × w. He wants to enlarge it so that it is possible to place a rectangle of size a × b on it (along the width or along the length, with sides parallel to the field sides). Find the minimum number of extensions needed to reach Arkady's goal.


-----Input-----

The first line contains five integers a, b, h, w and n (1 ≤ a, b, h, w, n ≤ 100 000) — the sizes of the rectangle needed to be placed, the initial sizes of the field and the number of available extensions.

The second line contains n integers a_1, a_2, ..., a_{n} (2 ≤ a_{i} ≤ 100 000), where a_{i} equals the integer a side multiplies by when the i-th extension is applied.


-----Output-----

Print the minimum number of extensions needed to reach Arkady's goal. If it is not possible to place the rectangle on the field with all extensions, print -1. If the rectangle can be placed on the initial field, print 0.


-----Examples-----
Input
3 3 2 4 4
2 5 4 10

Output
1

Input
3 3 3 3 5
2 3 5 4 2

Output
0

Input
5 5 1 2 3
2 2 3

Output
-1

Input
3 4 1 1 3
2 3 2

Output
3



-----Note-----

In the first example it is enough to use any of the extensions available. For example, we can enlarge h in 5 times using the second extension. Then h becomes equal 10 and it is now possible to place the rectangle on the field.
"""

def min_extensions_needed(a: int, b: int, h: int, w: int, n: int, extensions: list[int]) -> int:
    def isin(a, b, h, w):
        return h >= a and w >= b or (h >= b and w >= a)
    
    extensions.sort(reverse=True)
    
    if isin(a, b, h, w):
        return 0
    
    vis = {h: w}
    
    for i in range(len(extensions)):
        nc = extensions[i]
        pairs = []
        
        for l in list(vis.keys()):
            pair = (l, vis[l] * nc)
            if isin(a, b, pair[0], pair[1]):
                return i + 1
            pairs.append(pair)
            
            if nc * l not in vis or vis[l] > vis[nc * l]:
                pair = (nc * l, vis[l])
                if isin(a, b, pair[0], pair[1]):
                    return i + 1
                pairs.append(pair)
        
        for p in pairs:
            vis[p[0]] = p[1]
    
    return -1