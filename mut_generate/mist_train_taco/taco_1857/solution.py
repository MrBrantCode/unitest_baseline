"""
QUESTION:
Example

Input

2 2 2 0 0 0 5


Output

1 3 3 1 0
"""

def calculate_output(X, Y, Z, A, B, C, N):
    S = [0] * max(2 * (X + Y + Z + 1), 2 * N + 2)
    for k in range(N):
        S[k] = k * (k + 1) // 2
    for k in range(N, X + Y + Z + 1):
        S[k] = k * (k + 1) // 2 + S[k - N]

    def calc(k, x, y, z):
        return S[k] - S[k - x] - S[k - y] - S[k - z] + S[k - (x + y)] + S[k - (y + z)] + S[k - (z + x)] - S[k - (x + y + z)]
    
    ans = [0] * N
    for b in range(N):
        k = (X + Y + Z - b - 1) // N * N + b
        ans[b] = calc(k + 1, X - A, Y - B, Z - C) + calc(k, A, Y - B, Z - C) + calc(k, X - A, B, Z - C) + calc(k, X - A, Y - B, C) + calc(k - 1, A, B, Z - C) + calc(k - 1, X - A, B, C) + calc(k - 1, A, Y - B, C) + calc(k - 2, A, B, C)
    
    return ans