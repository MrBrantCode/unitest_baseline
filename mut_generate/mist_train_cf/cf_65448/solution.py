"""
QUESTION:
Implement the function `will_it_fly(q, w, n, p)`: Given an array of integers `q`, determine if it can attain elevation based on the following conditions:
- `q` must be a palindromic array.
- The sum of elements in `q` must be less than or equal to the maximum total weight `w`.
- `q` must contain exactly `n` unique smallest digits.
- `q` must contain at least `p` number of prime numbers.
The function should handle larger arrays efficiently.
"""

def will_it_fly(q, w, n, p):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # check if q is palindromic
    if q != q[::-1]:
        return False

    # check if the sum of elements is less than w
    if sum(q) > w:
        return False

    # check if q contains exactly n unique smallest digits
    sorted_q = sorted(set(q))
    if len(sorted_q) != n or sorted_q[0] != min(q):
        return False
    
    # check if q contains at least p prime numbers
    prime_count = sum(1 for i in q if is_prime(i))
    if prime_count < p:
        return False

    return True