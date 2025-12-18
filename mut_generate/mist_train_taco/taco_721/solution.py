"""
QUESTION:
Example

Input

3
y 7
y 6
n 5


Output

1
"""

def calculate_max_yes_responses(N, responses):
    L = [+(l == 'y') for l, d in responses]
    D = [d for l, d in responses]
    
    ans = 0
    I = list(range(N))
    I.sort(key=D.__getitem__)
    U = [0] * N
    
    for i in I:
        if not L[i] or U[i]:
            continue
        d = D[i]
        U[i] = 1
        ans += 1
        k = i - 1
        while k >= 0 and (L[k] or D[k] < d):
            if L[k]:
                U[k] = 1
            k -= 1
        k = i + 1
        while k < N and (L[k] or D[k] < d):
            if L[k]:
                U[k] = 1
            k += 1
    
    return ans