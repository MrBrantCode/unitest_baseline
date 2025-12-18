"""
QUESTION:
Number of tanka

Wishing to die in the spring under the flowers

This is one of the famous tanka poems that Saigyo Hoshi wrote. Tanka is a type of waka poem that has been popular in Japan for a long time, and most of it consists of five phrases and thirty-one sounds of 5, 7, 5, 7, and 7.

By the way, the number 57577 consists of two types, 5 and 7. Such a positive integer whose decimal notation consists of exactly two types of numbers is called a tanka number. For example, 10, 12, 57577, 25252 are tanka numbers, but 5, 11, 123, 20180701 are not tanka songs.

A positive integer N is given. Find the Nth smallest tanka number.

Input

The input consists of up to 100 datasets. Each dataset is represented in the following format.

> N

The integer N satisfies 1 ≤ N ≤ 1018.

The end of the input is represented by a single zero line.

Output

For each dataset, output the Nth smallest tanka number on one line.

Sample Input


1
2
3
390
1124
1546
314159265358979323
0


Output for the Sample Input


Ten
12
13
2020
25252
57577
7744444777744474777777774774744777747477444774744744






Example

Input

1
2
3
390
1124
1546
314159265358979323
0


Output

10
12
13
2020
25252
57577
7744444777744474777777774774744777747477444774744744
"""

def find_nth_tanka_number(N: int, cl: list) -> str:
    k = 0
    rng = 0
    for i in range(54):
        if cl[i] < N <= cl[i + 1]:
            k = i + 2
            rng2 = cl[i]
            rng = cl[i + 1] - cl[i]
    
    posrng = (N - rng2) % (rng // 9)
    perrng = (N - rng2) // (rng // 9) + 1
    
    if posrng == 0:
        posrng = rng // 9
        perrng -= 1
    
    ans = [perrng]
    for i in range(k - 1):
        if i == k - 2:
            tmp = [0 if j == perrng else 1 for j in range(10)]
        else:
            tmp = [(cl[k - i - 2] - cl[k - i - 3]) // 9 if j == perrng else 2 ** (k - i - 2) for j in range(10)]
        
        if posrng <= tmp[0]:
            ans.append(0)
        for j in range(1, 10):
            tmp[j] += tmp[j - 1]
            if tmp[j - 1] < posrng <= tmp[j]:
                ans.append(j)
                posrng -= tmp[j - 1]
        
        if max(ans) != min(ans):
            break
    
    for i in range(k - len(ans), 0, -1):
        if posrng <= 2 ** (i - 1):
            ans.append(min(ans))
        else:
            ans.append(max(ans))
            posrng -= 2 ** (i - 1)
    
    return ''.join(map(str, ans))

# Precomputation of cl list
cl = [sum([9 * 2 ** j for j in range(i)]) * 9 for i in range(55)]
for i in range(1, 55):
    cl[i] += cl[i - 1]