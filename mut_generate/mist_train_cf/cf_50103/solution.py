"""
QUESTION:
Create a function `verify_user_credentials` that authenticates user credentials using Hash-based Message Authentication Code (HMAC) with Salted Password Hashing. The function should handle exceptions and errors effectively and log all login attempts. It should support multi-factor authentication process.

The function should take `user_identity` and `password` as input, hash the password using a randomly generated salt, and compare it with the stored hashed password. If the passwords match, log a successful authentication attempt; otherwise, log a failed attempt. The function should also have a limit on the number of failed login attempts.

Note: The function should not log sensitive information like passwords.
"""

import hashlib
import hmac
import logging

def verify_user_credentials(user_identity: str, password: str, salt: bytes, user_hash: bytes, max_attempts: int = 3) -> bool:
    """
    Authenticate user credentials using Hash-based Message Authentication Code (HMAC) with Salted Password Hashing.

    Args:
        user_identity (str): Unique user identification.
        password (str): User's password.
        salt (bytes): Randomly generated salt.
        user_hash (bytes): Stored hashed password.
        max_attempts (int, optional): Maximum number of failed login attempts. Defaults to 3.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """

    logging.basicConfig(filename='auth.log', level=logging.INFO, 
                        format='%(asctime)s:%(levelname)s:%(message)s')

    attempts = 0
    while attempts < max_attempts:
        entered_password = password
        entered_hash = hashlib.pbkdf2_hmac('sha256', entered_password.encode(), salt, 100000)
        
        if hmac.compare_digest(user_hash, entered_hash):
            logging.info(f'User {user_identity} is authenticated.')
            return True
        else:
            logging.warning(f'Failed login attempt for user {user_identity}')
            attempts += 1
    return False