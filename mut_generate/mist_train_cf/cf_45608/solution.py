"""
QUESTION:
Create a function `crackSafe` that takes four parameters: `n`, `k`, `m`, and `lock_sequence`. The function should return a string representing the minimal possible password of length `k^n` that guarantees unlocking the receptacle without triggering the permanent lock. The parameters have the following constraints:
- `n` is an integer between 1 and 4 (inclusive)
- `m` is an integer between 1 and `n` (inclusive)
- `k` is an integer between 1 and 10 (inclusive)
- `k^n` does not exceed 4096
- `lock_sequence` is a string of length `m` consisting of numerals from 0 to `k-1` (inclusive), which is not a suffix of the password.
"""

def crackSafe(n, k, m, lock_sequence):
    """
    This function generates the minimal possible password of length k^n 
    that guarantees unlocking the receptacle without triggering the permanent lock.

    Parameters:
    n (int): The length of the password string.
    k (int): The base of the number system.
    m (int): The length of the lock sequence.
    lock_sequence (str): The lock sequence string.

    Returns:
    str: The minimal possible password string.
    """
    
    # Generate de Bruijn sequence
    alphabet = list(map(str, range(k)))
    sequence = []
    a = [0] * k * n
    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p+1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    
    # Join the sequence into a string
    password = ''.join(alphabet[i] for i in sequence)
    
    # Remove the lock sequence if it exists
    if password.endswith(lock_sequence):
        password = password[:-m] + password[-m:].replace(lock_sequence, '')
    
    # Ensure the password length is k^n
    password = password[:k**n]
    
    return password