"""
QUESTION:
Implement the `is_complete` method to determine if a complete message has been received based on the presence of the end-of-message byte '\x04'. The method should return `True` if a complete message is received and `False` otherwise. The end-of-message index can be obtained using the existing `get_eom_idx` method. Assume that `self.message` contains the received bytes and `self.get_eom_idx` returns the index of the end-of-message byte.
"""

def is_complete(self):
    eom_idx = self.get_eom_idx()
    if not eom_idx:
        return False
    received = self.message.keys()
    return all(idx < eom_idx for idx in received)