"""
QUESTION:
Create a function `validate_signature` and a Flask endpoint `/webhook` that can parse different types of data (XML, JSON, Text) received from the webhook requests. The `/webhook` endpoint should be able to validate the request's signature using the provided `validate_signature` function to ensure it is received from a trusted source. The function should use a secret key for HMAC hashing. The endpoint should reply to the request with appropriate response codes. 

Implement error logging and restrict the `SECRET_KEY` to be used for HMAC hashing. The endpoint should accept POST requests and support parsing of XML, JSON, and Plain Text data based on the `request.mimetype`. The data should be logged using Python's logging module. The function `validate_signature` should return `True` if the signature is valid, `False` otherwise.
"""

def validate_signature(sig_header, data, secret_key):
    """
    Validate the signature of the received data using the provided secret key.

    Args:
        sig_header (str): The 'X-Hub-Signature' header received in the request.
        data (bytes): The data received in the request.
        secret_key (str): The secret key used for HMAC hashing.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    signature = 'sha1=' + hmac.new(
        key=secret_key.encode(),
        msg=data,
        digestmod=hashlib.sha1
    ).hexdigest()

    return hmac.compare_digest(signature, sig_header)