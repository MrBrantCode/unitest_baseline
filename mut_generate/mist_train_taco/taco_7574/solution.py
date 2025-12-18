"""
QUESTION:
Pasha has a positive integer a without leading zeroes. Today he decided that the number is too small and he should make it larger. Unfortunately, the only operation Pasha can do is to swap two adjacent decimal digits of the integer.

Help Pasha count the maximum number he can get if he has the time to make at most k swaps.


-----Input-----

The single line contains two integers a and k (1 ≤ a ≤ 10^18; 0 ≤ k ≤ 100).


-----Output-----

Print the maximum number that Pasha can get if he makes at most k swaps.


-----Examples-----
Input
1990 1

Output
9190

Input
300 0

Output
300

Input
1034 2

Output
3104

Input
9090000078001234 6

Output
9907000008001234
"""

def maximize_number_with_swaps(a: str, k: int) -> str:
    a = list(a)
    b = sorted(a, reverse=True)
    
    for i in range(len(a)):
        for x in b:
            if a[i] == x:
                break
            j = a.index(x, i)
            if j - i > k:
                continue
            k -= j - i
            a[i:j + 1] = [a[j]] + a[i:j]
            break
        b.remove(a[i])
    
    return ''.join(a)