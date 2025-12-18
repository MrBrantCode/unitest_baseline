"""
QUESTION:
Implement the `decode_basic_auth_token` function that takes a non-empty base64-encoded string as input and returns a tuple containing the decoded username and password. The function should raise a custom `BasicAuthException` with the original exception as the cause if any exceptions occur during the decoding process, including `binascii.Error` for invalid base64-encoded strings, `ValueError` for invalid username:password pairs, and `TypeError` for any other decoding errors.
"""

import base64

class BasicAuthException(Exception):
    pass

def decode_basic_auth_token(b_token):
    try:
        auth_pair = base64.b64decode(b_token, validate=True).decode('utf-8')
        username, password = auth_pair.split(':')
        return (username, password)
    except base64.binascii.Error as e:
        raise BasicAuthException("Invalid base64-encoded token") from e
    except ValueError as e:
        raise BasicAuthException("Invalid username:password format") from e
    except TypeError as e:
        raise BasicAuthException("Error occurred during decoding") from e