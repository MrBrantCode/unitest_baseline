"""
QUESTION:
Implement the `encrypt(alpha, n, e)` and `decrypt(beta, n, d)` functions for a simplified encryption and decryption algorithm using modular arithmetic and exponentiation. 

The `encrypt(alpha, n, e)` function should take a plaintext `alpha`, a public key `n`, and a public exponent `e` as input and return the ciphertext `beta` using the formula `beta = (alpha % n)^e % n`. 

The `decrypt(beta, n, d)` function should take a ciphertext `beta`, a public key `n`, and a private key `d` as input and return the decrypted plaintext `alpha` using the formula `alpha = beta^d % n`. 

Assume all input values are positive integers and the encryption and decryption keys are valid for the given context.
"""

def entrance(alpha, n, e):
    ctt = alpha % n
    return pow(ctt, e, n)