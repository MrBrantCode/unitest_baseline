"""
QUESTION:
Write a function `is_bounded_black_scholes_greek(n, T, t, S, K, r, sigma, q)` that takes the order of derivative `n`, time to maturity `T-t`, current spot price `S`, strike price `K`, risk-free interest rate `r`, volatility `sigma`, and dividend yield `q` as inputs and returns `False` to indicate that the absolute value of the n-th derivative of the Black-Scholes option price with respect to `x = log S` is not bounded by some expression of the form `M(T-t)^m(n)` with `M` independent of `T`, `t` and `S`.
"""

def is_bounded_black_scholes_greek(n, T, t, S, K, r, sigma, q):
    return False