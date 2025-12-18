"""
QUESTION:
You are given an array $a$ consisting of $n$ integer numbers.

You have to color this array in $k$ colors in such a way that:   Each element of the array should be colored in some color;  For each $i$ from $1$ to $k$ there should be at least one element colored in the $i$-th color in the array;  For each $i$ from $1$ to $k$ all elements colored in the $i$-th color should be distinct. 

Obviously, such coloring might be impossible. In this case, print "NO". Otherwise print "YES" and any coloring (i.e. numbers $c_1, c_2, \dots c_n$, where $1 \le c_i \le k$ and $c_i$ is the color of the $i$-th element of the given array) satisfying the conditions above. If there are multiple answers, you can print any.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le k \le n \le 5000$) — the length of the array $a$ and the number of colors, respectively.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 5000$) — elements of the array $a$.


-----Output-----

If there is no answer, print "NO". Otherwise print "YES" and any coloring (i.e. numbers $c_1, c_2, \dots c_n$, where $1 \le c_i \le k$ and $c_i$ is the color of the $i$-th element of the given array) satisfying the conditions described in the problem statement. If there are multiple answers, you can print any.


-----Examples-----
Input
4 2
1 2 2 3

Output
YES
1 1 2 2

Input
5 2
3 2 1 2 3

Output
YES
2 1 1 2 1

Input
5 2
2 1 1 2 1

Output
NO



-----Note-----

In the first example the answer $2~ 1~ 2~ 1$ is also acceptable.

In the second example the answer $1~ 1~ 1~ 2~ 2$ is also acceptable.

There exist other acceptable answers for both examples.
"""

def color_array(n, k, arr):
    dict1 = {}
    for i in range(n):
        try:
            dict1[arr[i]].append(i)
        except KeyError:
            dict1[arr[i]] = [i]
    
    flag = 0
    colors = {}
    for i in dict1.keys():
        colors[i] = [0] * k
        if len(dict1[i]) > k:
            flag = 1
            break
    
    if flag == 1:
        return "NO", None
    
    ansarr = [0] * n
    for i in range(k):
        ansarr[i] = i + 1
        colors[arr[i]][i] = 1
    
    val = 0
    for i in dict1.keys():
        for j in dict1[i]:
            if ansarr[j] == 0:
                for l in range(k):
                    if colors[i][l] == 0:
                        ansarr[j] = l + 1
                        colors[i][l] = 1
                        break
    
    return "YES", ansarr