"""
QUESTION:
Create a Python function named `extract_jwt_claims` that takes in three parameters: `jwt`, `user_given_name`, and `user_family_name`. The function should extract specific claims from the given JSON Web Token (JWT) and return them as a dictionary. The extracted claims include "nonce", "aud", "acr", "nsAccountLock", "eduPersonScopedAffiliation", "auth_time", "name", "schacHomeOrganization", "exp", "iat", and "family_name". The "eduPersonScopedAffiliation", "name", and "family_name" claims should be updated with the provided user information.
"""

import base64
import json

def extract_jwt_claims(jwt: str, user_given_name: str, user_family_name: str) -> dict:
    # Split the JWT into its three parts: header, payload, and signature
    header, payload, _ = jwt.split('.')

    # Decode the payload from base64 and convert it to a dictionary
    decoded_payload = base64.urlsafe_b64decode(payload + '===').decode('utf-8')
    jwt_claims = json.loads(decoded_payload)

    # Update specific claims with user information
    jwt_claims["eduPersonScopedAffiliation"] = f"{user_given_name};{user_family_name}"
    jwt_claims["name"] = f"{user_given_name} {user_family_name}"
    jwt_claims["family_name"] = user_family_name

    return jwt_claims