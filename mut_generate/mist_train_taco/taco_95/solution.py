"""
QUESTION:
Vasya had an array of $n$ integers, each element of the array was from $1$ to $n$. He chose $m$ pairs of different positions and wrote them down to a sheet of paper. Then Vasya compared the elements at these positions, and wrote down the results of the comparisons to another sheet of paper. For each pair he wrote either "greater", "less", or "equal".

After several years, he has found the first sheet of paper, but he couldn't find the second one. Also he doesn't remember the array he had. In particular, he doesn't remember if the array had equal elements. He has told this sad story to his informatics teacher Dr Helen.

She told him that it could be the case that even if Vasya finds his second sheet, he would still not be able to find out whether the array had two equal elements. 

Now Vasya wants to find two arrays of integers, each of length $n$. All elements of the first array must be distinct, and there must be two equal elements in the second array. For each pair of positions Vasya wrote at the first sheet of paper, the result of the comparison must be the same for the corresponding elements of the first array, and the corresponding elements of the second array. 

Help Vasya find two such arrays of length $n$, or find out that there are no such arrays for his sets of pairs.


-----Input-----

The first line of input contains two integers $n$, $m$ — the number of elements in the array and number of comparisons made by Vasya ($1 \le n \le 100\,000$, $0 \le m \le 100\,000$).

Each of the following $m$ lines contains two integers $a_i$, $b_i$  — the positions of the $i$-th comparison ($1 \le a_i, b_i \le n$; $a_i \ne b_i$). It's guaranteed that any unordered pair is given in the input at most once.


-----Output-----

The first line of output must contain "YES" if there exist two arrays, such that the results of comparisons would be the same, and all numbers in the first one are distinct, and the second one contains two equal numbers. Otherwise it must contain "NO".

If the arrays exist, the second line must contain the array of distinct integers, the third line must contain the array, that contains at least one pair of equal elements. Elements of the arrays must be integers from $1$ to $n$.


-----Examples-----
Input
1 0

Output
NO

Input
3 1
1 2

Output
YES
1 3 2 
1 3 1 

Input
4 3
1 2
1 3
2 4

Output
YES
1 3 4 2 
1 3 4 1
"""

def find_vasya_arrays(n, m, comparisons):
    if n == 1:
        return "NO", None, None
    
    c = [[0, i, []] for i in range(n)]
    for a, b in comparisons:
        c[a - 1][0] += 1
        c[a - 1][2].append(b - 1)
        c[b - 1][0] += 1
        c[b - 1][2].append(a - 1)
    
    ans = n * (n - 1) // 2
    if m >= ans:
        return "NO", None, None
    
    c.sort(key=lambda x: x[0])
    vall = c[0][1]
    c[0][2].append(vall)
    c[0][2].sort()
    
    final = -1
    for i in range(len(c[0][2])):
        if c[0][2][i] != i and i != vall:
            final = i
            break
    if final == -1:
        final = len(c[0][2])
    
    s1 = []
    s2 = []
    val = 1
    temp = min(vall, final)
    temp2 = max(vall, final)
    
    for i in range(n):
        if i == temp:
            s1.append(n)
            s2.append(n)
        elif i == temp2:
            s1.append(n - 1)
            s2.append(n)
        else:
            s1.append(val)
            s2.append(val)
            val += 1
    
    return "YES", s1, s2