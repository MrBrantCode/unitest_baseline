"""
QUESTION:
Design a data structure to store client records, where each record includes the client's name, address, phone number, email, occupation, transaction history, and recommendations. The data structure should allow for efficient retrieval of a client's record by name.
"""

class ClientRecord:
    def __init__(self, name, address, phone, email, occupation, transaction_history, recommendations):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.occupation = occupation
        self.transaction_history = transaction_history
        self.recommendations = recommendations

def entrance(name, address, phone, email, occupation, transaction_history, recommendations):
    """
    Creates a client record with given parameters.
    """
    return ClientRecord(name, address, phone, email, occupation, transaction_history, recommendations)