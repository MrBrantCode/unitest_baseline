"""
QUESTION:
Construct a function `construct_secure_json` that takes five parameters: `a2_admin`, `a2_password`, `a2_admin_token`, `a2_ingest_token`, and `a2_url`. The function should construct a JSON object containing these parameters, but replace the `a2_password` value with asterisks for security. The function should return the constructed JSON object.
"""

import json

def construct_secure_json(a2_admin, a2_password, a2_admin_token, a2_ingest_token, a2_url):
    secure_json = {
        "a2_admin": a2_admin,
        "a2_password": "*" * len(a2_password),  
        "a2_admin_token": a2_admin_token,
        "a2_ingest_token": a2_ingest_token,
        "a2_url": a2_url
    }
    return json.dumps(secure_json)