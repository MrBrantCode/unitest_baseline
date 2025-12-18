"""
QUESTION:
The `generate_transaction_id` function generates a unique identifier for a financial transaction record. The function takes a `Transaction` object as input with attributes `date`, `amount`, `trntype`, `payee`, and `memo`. The function should calculate a unique identifier by hashing the concatenation of the string representations of the transaction attributes using the SHA-256 hashing algorithm and assign the hashed value to the `id` attribute of the `Transaction` object.
"""

import hashlib

def generate_transaction_id(transaction):
    h = hashlib.sha256()
    h.update(str(transaction.date).encode('utf-8'))
    h.update(str(transaction.amount).encode('utf-8'))
    h.update(str(transaction.trntype).encode('utf-8'))
    h.update(str(transaction.payee).encode('utf-8'))
    h.update(str(transaction.memo).encode('utf-8'))

    transaction.id = h.hexdigest()

    return transaction