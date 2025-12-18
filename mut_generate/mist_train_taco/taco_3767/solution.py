"""
QUESTION:
You are given N natural numbers and K swaps are allowed. Determine the largest permutation that you can attain.

INPUT:
First line contains N and k
next line has N spaced integers

OUTPUT:
Print the largest permutation array.

0<N<10^5
0<K<10^5

SAMPLE INPUT
5 1
4 2 3 5 1

SAMPLE OUTPUT
5 2 3 4 1
"""

def largest_permutation(N, K, arr):
    x = 0
    while K > 0 and x < N:
        max_e = arr[x]
        swap_i = x
        for i in range(x, N):
            if arr[i] > max_e:
                max_e = arr[i]
                swap_i = i
        
        if swap_i != x:
            arr[x], arr[swap_i] = arr[swap_i], arr[x]
            K -= 1
        
        x += 1
    
    return arr