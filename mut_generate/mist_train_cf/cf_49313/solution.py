"""
QUESTION:
Construct a function `construct_array` that takes two arrays `A` and `B` as input. The function should apply a custom function `F(x, y)` on every pair of elements from arrays `A` and `B` and store the result in a new array `C`. The function `F(x, y)` is defined as follows:
- If `x` is even and `y` is odd, then `F(x, y) = (x^2) * (y^2)`
- If `x` is odd and `y` is even, then `F(x, y) = x * y * (x + y)`
- Otherwise, `F(x, y) = x * y`

Constraints:
- 1 ≤ length(A), length(B) ≤ 1000
- 0 ≤ A_i, B_i ≤ 10^4
"""

def construct_array(A, B):
    def F(x, y):
        if x % 2 == 0 and y % 2 == 1:
            return (x ** 2) * (y ** 2)
        elif x % 2 == 1 and y % 2 == 0:
            return x * y * (x + y)
        else:
            return x * y

    return [F(A[i], B[i]) for i in range(len(A))]