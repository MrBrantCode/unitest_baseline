"""
QUESTION:
Implement the function `foo(x, y, z, n)` to modify the third parameter 'z' based on the Fibonacci sequence up to 'n' terms. If 'z' appears in the Fibonacci sequence, set 'z' to 0; otherwise, keep 'z' as it is. The function should return the modified 'z' along with 'x', 'y', and 'n'.
"""

def entance(x, y, z, n):
    # Create a list of Fibonacci numbers up to n terms
    fibonacci = []
    a, b = 0, 1
    for i in range(n):
        fibonacci.append(a)
        a, b = b, a + b

    # If the third parameter 'z' is in the Fibonacci sequence, set it to '0'.
    # If it's not in the sequence, keep it as it is.
    z = 0 if z in fibonacci else z

    return x, y, z, n