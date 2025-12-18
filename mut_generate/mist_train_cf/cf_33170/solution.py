"""
QUESTION:
Implement the `verifySignature` method, which takes three parameters: `verificationKey` (the public key used for verification), `content` (the content whose signature needs to be verified), and `signature` (the signature to be verified). The method should return a boolean value indicating whether the signature is valid.
"""

import hashlib
import hmac

def verifySignature(verificationKey, content, signature):
    verificationEngine = hmac.new(verificationKey.encode(), digestmod=hashlib.sha256)
    verificationEngine.update(content.encode())
    return verificationEngine.hexdigest() == signature