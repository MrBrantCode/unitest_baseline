"""
QUESTION:
Implement a `Storage` class with a method `generate_url(expiration)` that generates a URL for accessing a file stored in cloud storage. The class should initialize with a `bucket` name, `file_key`, and an optional `endpoint`. The `generate_url` method should return a URL that includes the `endpoint` if provided and is valid for the specified `expiration` time in seconds.
"""

def generate_url(bucket, file_key, endpoint=None, expiration=None):
    if endpoint:
        return f"{endpoint}/{bucket}/{file_key}?expires={expiration}"
    else:
        return f"https://{bucket}.storage.com/{file_key}?expires={expiration}"