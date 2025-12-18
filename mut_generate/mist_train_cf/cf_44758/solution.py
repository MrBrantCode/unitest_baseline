"""
QUESTION:
Write a function `trisection(f, a, b, tol)` that finds a root of a given continuous cubic function `f(x)` in the interval `[a, b]` using the trisection method. The function should take as input the function `f`, the interval boundaries `a` and `b`, and a tolerance `tol`. It should return an approximation of a root within the specified tolerance. The function should assume that a root exists in the interval `[a, b]`, but if not, it should print a corresponding message and return `None`.
"""

def trisection(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("The function has the same sign at a and b. We don't guarantee that a root exists in this interval.")
        return
    while (b-a) >= tol:
        c1 = a + (b - a) / 3
        c2 = b - (b - a) / 3

        if f(c1) == 0:  
            return c1
        elif f(c2) == 0:  
            return c2
        elif f(a) * f(c1) < 0:  
            b = c1
        elif f(c2) * f(b) < 0:  
            a = c2
        else:  
            a = c1
            b = c2

    return (a + b) / 2