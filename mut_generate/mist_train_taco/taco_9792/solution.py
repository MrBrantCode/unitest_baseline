"""
QUESTION:
Hector the hacker has stolen some information, but it is encrypted. In order to decrypt it, he needs to write a function that will generate a decryption key from the encryption key which he stole (it is in hexadecimal). To do this, he has to determine the two prime factors `P` and `Q` of the encyption key, and return the product `(P-1) * (Q-1)`.

**Note:** the primes used are < 10^(5)

## Examples

For example if the encryption key is `"47b"`, it is 1147 in decimal. This factors to 31\*37, so the key Hector needs is 1080 (= 30\*36).


More examples:
* input: `"2533"`, result: 9328 (primes: 89, 107)
* input: `"1ba9"`, result: 6912 (primes: 73, 97)
"""

def generate_decryption_key(encryption_key: str) -> int:
    """
    Generates a decryption key from the given encryption key in hexadecimal format.

    Args:
        encryption_key (str): The encryption key in hexadecimal format.

    Returns:
        int: The decryption key, which is the product of (P-1) * (Q-1) where P and Q are the prime factors of the encryption key.
    """
    n = int(encryption_key, 16)
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            P = k
            Q = n // k
            return (P - 1) * (Q - 1)
    return None  # In case no prime factors are found (though per problem statement, this should not happen)